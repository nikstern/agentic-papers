from __future__ import annotations

import csv
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from ollama_embedder import (
    DEFAULT_OLLAMA_BASE_URL,
    DEFAULT_OLLAMA_BATCH_SIZE,
    DEFAULT_OLLAMA_TIMEOUT,
    OllamaEmbedder,
)
from qdrant_client import QdrantClient
import yaml


ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "paper_inbox" / "papers.csv"
ENRICHMENT_DIR = ROOT / "paper_inbox" / "enrichment"
NOTES_DIR = ROOT / "paper_notes"
DEFAULT_COLLECTION = "agentic-papers"
DEFAULT_MODEL = "embeddinggemma:300m"
DEFAULT_LOCAL_PATH = ROOT / "search" / ".qdrant"
DEFAULT_QDRANT_MODE = "server"
DEFAULT_QDRANT_URL = "http://127.0.0.1:6333"
DEFAULT_QDRANT_TIMEOUT = 5.0
ALLOWED_QDRANT_MODES = {"server", "embedded"}
SECTION_ORDER = {
    "summary": 1,
    "why_it_matters": 2,
    "method_setup": 3,
    "key_claims": 4,
    "limitations": 5,
    "full_context": 6,
}


@dataclass
class IndexedSection:
    point_id: int
    paper_id: int
    title: str
    candidate_topic: str
    paper_type: str
    year: int
    status: str
    enrichment_status: str
    authors: str
    source: str
    url: str
    section: str
    path: str
    text: str


@dataclass
class PaperRecord:
    paper_id: int
    title: str
    year: int
    candidate_topic: str
    paper_type: str
    status: str
    enrichment_status: str
    authors: str
    source: str
    url: str
    path: str
    frontmatter: dict


def get_collection_name() -> str:
    return os.environ.get("QDRANT_COLLECTION", DEFAULT_COLLECTION)


def get_model_name() -> str:
    return os.environ.get("EMBEDDING_MODEL", DEFAULT_MODEL)


def get_local_path() -> Path:
    raw = os.environ.get("QDRANT_LOCAL_PATH")
    if raw:
        return Path(raw).expanduser().resolve()
    return DEFAULT_LOCAL_PATH


def get_backend_mode() -> str:
    mode = os.environ.get("QDRANT_MODE", DEFAULT_QDRANT_MODE).strip().lower()
    if mode not in ALLOWED_QDRANT_MODES:
        allowed = ", ".join(sorted(ALLOWED_QDRANT_MODES))
        raise ValueError(f"QDRANT_MODE must be one of: {allowed}")
    return mode


def get_server_url() -> str:
    url = os.environ.get("QDRANT_URL", DEFAULT_QDRANT_URL).strip().rstrip("/")
    if not url:
        raise ValueError("QDRANT_URL cannot be empty in server mode")
    return url


def get_timeout() -> float:
    raw = os.environ.get("QDRANT_TIMEOUT")
    if raw is None:
        return DEFAULT_QDRANT_TIMEOUT
    try:
        timeout = float(raw)
    except ValueError as exc:
        raise ValueError("QDRANT_TIMEOUT must be a positive number") from exc
    if timeout <= 0:
        raise ValueError("QDRANT_TIMEOUT must be a positive number")
    return timeout


def get_client() -> QdrantClient:
    if get_backend_mode() == "embedded":
        return QdrantClient(path=str(get_local_path()))
    return QdrantClient(
        url=get_server_url(),
        api_key=os.environ.get("QDRANT_API_KEY"),
        timeout=get_timeout(),
    )


def require_client() -> QdrantClient:
    client = get_client()
    try:
        client.get_collections()
    except Exception as exc:
        if get_backend_mode() == "embedded":
            raise
        raise RuntimeError(
            f"Qdrant server is unavailable at {get_server_url()}. "
            "Start it with `make search-server-up`, or explicitly use "
            "`QDRANT_MODE=embedded` for single-process local mode."
        ) from exc
    return client


def get_embedder() -> OllamaEmbedder:
    return OllamaEmbedder(
        base_url=os.environ.get("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL),
        model=get_model_name(),
        batch_size=int(
            os.environ.get("OLLAMA_BATCH_SIZE", str(DEFAULT_OLLAMA_BATCH_SIZE))
        ),
        timeout=float(os.environ.get("OLLAMA_TIMEOUT", str(DEFAULT_OLLAMA_TIMEOUT))),
    )


def load_rows() -> list[dict[str, str]]:
    with INBOX.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_enrichment(paper_id: str) -> dict:
    path = ENRICHMENT_DIR / f"{paper_id}.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_text(value: str) -> str:
    lowered = value.strip().lower()
    cleaned = re.sub(r"[^a-z0-9]+", " ", lowered)
    return " ".join(cleaned.split())


def slug_title(title: str) -> str:
    cleaned = []
    for char in title:
        if char.isalnum() or char.isspace() or char in {"_", "-"}:
            cleaned.append(char)
    normalized = " ".join("".join(cleaned).split())
    words = normalized.split()
    return "-".join(words[:8]).strip("-") or "Untitled"


def note_path(year: str, title: str) -> Path:
    return NOTES_DIR / f"{year}-{slug_title(title)}.md"


def load_note_frontmatter(path: Path) -> dict:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}
    data = yaml.safe_load(parts[1]) or {}
    if not isinstance(data, dict):
        return {}
    return data


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return text
    return parts[2].lstrip()


def load_note_text(year: str, title: str) -> str:
    path = note_path(year, title)
    if not path.exists():
        return ""
    return strip_frontmatter(path.read_text(encoding="utf-8")).strip()


def load_paper_records() -> list[PaperRecord]:
    records: list[PaperRecord] = []
    for row in load_rows():
        path = note_path(row["year"], row["title"])
        frontmatter = load_note_frontmatter(path)
        records.append(
            PaperRecord(
                paper_id=int(row["paper_id"]),
                title=row["title"],
                year=int(row["year"]),
                candidate_topic=row["candidate_topic"],
                paper_type=row["paper_type"],
                status=row["status"],
                enrichment_status=row["enrichment_status"],
                authors=row["authors"],
                source=row["source"],
                url=row["url"],
                path=str(path.relative_to(ROOT)),
                frontmatter=frontmatter,
            )
        )
    return records


def paper_aliases(title: str) -> set[str]:
    note_stem = f"{title}"
    aliases = {
        title,
        normalize_text(title),
        slug_title(title).replace("-", " "),
    }
    if ":" in title:
        prefix = title.split(":", 1)[0].strip()
        aliases.add(prefix)
        aliases.add(normalize_text(prefix))
    words = title.split()
    if words:
        aliases.add(words[0])
        aliases.add(normalize_text(words[0]))
    return {alias for alias in aliases if alias}


def record_aliases(record: PaperRecord) -> set[str]:
    path = Path(record.path)
    stem = path.stem
    aliases = set(paper_aliases(record.title))
    aliases.add(stem)
    aliases.add(normalize_text(stem))
    aliases.add(f"{record.year} {record.title}")
    aliases.add(normalize_text(f"{record.year} {record.title}"))
    return {alias for alias in aliases if alias}


def build_sections(row: dict[str, str]) -> list[IndexedSection]:
    paper_id = row["paper_id"]
    enrichment = load_enrichment(paper_id)
    note_text = load_note_text(row["year"], row["title"])
    note_rel = note_path(row["year"], row["title"]).relative_to(ROOT)

    section_texts = {
        "summary": enrichment.get("summary", ""),
        "why_it_matters": enrichment.get("why_it_matters", ""),
        "method_setup": enrichment.get("method_setup", ""),
        "key_claims": "\n".join(enrichment.get("key_claims", [])),
        "limitations": "\n".join(enrichment.get("limitations", [])),
    }
    full_context_parts = [
        row["title"],
        row["candidate_topic"],
        section_texts["summary"],
        section_texts["why_it_matters"],
        section_texts["method_setup"],
        section_texts["key_claims"],
        section_texts["limitations"],
        note_text,
    ]
    section_texts["full_context"] = "\n\n".join(part for part in full_context_parts if part)

    sections: list[IndexedSection] = []
    for section, text in section_texts.items():
        normalized = text.strip()
        if not normalized:
            continue
        sections.append(
            IndexedSection(
                point_id=int(paper_id) * 10 + SECTION_ORDER[section],
                paper_id=int(paper_id),
                title=row["title"],
                candidate_topic=row["candidate_topic"],
                paper_type=row["paper_type"],
                year=int(row["year"]),
                status=row["status"],
                enrichment_status=row["enrichment_status"],
                authors=row["authors"],
                source=row["source"],
                url=row["url"],
                section=section,
                path=str(note_rel),
                text=normalized,
            )
        )
    return sections


def iter_sections(rows: Iterable[dict[str, str]]) -> Iterable[IndexedSection]:
    for row in rows:
        yield from build_sections(row)
