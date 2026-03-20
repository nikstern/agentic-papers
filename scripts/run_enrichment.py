#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from html import unescape
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
QUEUE_PATH = ROOT / "paper_inbox" / "approved_for_enrichment.json"
OUTPUT_PATH = ROOT / "paper_inbox" / "auto_enrichment_output.json"
INBOX = ROOT / "paper_inbox" / "papers.csv"
DEFAULT_MODEL = "gpt-4.1-mini"
MAX_SOURCE_CHARS = 120_000
FIELDNAMES = [
    "paper_id",
    "title",
    "url",
    "year",
    "authors",
    "candidate_topic",
    "source",
    "paper_type",
    "status",
    "enrichment_status",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run automatic paper enrichment for pending vault papers."
    )
    parser.add_argument(
        "--input",
        default=str(QUEUE_PATH),
        help="path to approved_for_enrichment style input JSON",
    )
    parser.add_argument(
        "--output",
        default=str(OUTPUT_PATH),
        help="path to write enrichment JSON array",
    )
    parser.add_argument(
        "--ids",
        nargs="*",
        help="optional paper IDs to enrich from the queue",
    )
    return parser.parse_args()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_rows() -> list[dict[str, str]]:
    with INBOX.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDNAMES:
            fail("papers.csv header does not match expected schema")
        return list(reader)


def get_paper_row_map() -> dict[str, dict[str, str]]:
    return {row["paper_id"]: row for row in load_rows()}


def normalize_spaces(text: str) -> str:
    return " ".join(text.split())


def strip_html(raw_html: str) -> str:
    text = re.sub(r"(?is)<script.*?>.*?</script>", " ", raw_html)
    text = re.sub(r"(?is)<style.*?>.*?</style>", " ", text)
    text = re.sub(r"(?is)<[^>]+>", " ", text)
    return normalize_spaces(unescape(text))


def fetch_text(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "AgenticVault/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="ignore")


def arxiv_id_from_url(url: str) -> str | None:
    match = re.search(r"arxiv\.org/(?:abs|pdf)/([^/?#]+)", url)
    if not match:
        return None
    return match.group(1).replace(".pdf", "")


def extract_arxiv_abstract(html: str) -> str:
    match = re.search(
        r'(?is)<blockquote[^>]*class="abstract[^"]*"[^>]*>(.*?)</blockquote>',
        html,
    )
    if not match:
        return ""
    abstract = strip_html(match.group(1))
    abstract = re.sub(r"^Abstract:\s*", "", abstract, flags=re.IGNORECASE)
    return abstract


def paper_source_text(title: str, url: str) -> str:
    arxiv_id = arxiv_id_from_url(url)
    chunks: list[str] = [f"Title: {title}", f"URL: {url}"]

    if arxiv_id:
        abs_url = f"https://arxiv.org/abs/{arxiv_id}"
        try:
            abs_html = fetch_text(abs_url)
            abstract = extract_arxiv_abstract(abs_html)
            if abstract:
                chunks.append(f"Abstract: {abstract}")
        except urllib.error.URLError:
            pass

        html_url = f"https://arxiv.org/html/{arxiv_id}"
        try:
            html_text = fetch_text(html_url)
            rendered = strip_html(html_text)
            if rendered:
                chunks.append(f"Paper text: {rendered[:MAX_SOURCE_CHARS]}")
        except urllib.error.URLError:
            pass

    if len(chunks) == 2:
        chunks.append("No remote paper text could be fetched.")

    return "\n\n".join(chunks)[:MAX_SOURCE_CHARS]


def prompt_for_paper(row: dict[str, str], source_text: str) -> str:
    return f"""
You are enriching a research paper note for an Obsidian vault.

Return valid JSON only with this exact schema:
{{
  "paper_id": {int(row["paper_id"])},
  "summary": "string",
  "why_it_matters": "string",
  "method_setup": "string",
  "key_claims": ["string"],
  "limitations": ["string"],
  "evaluates": ["string"],
  "builds_on_unresolved": ["string"],
  "compares_to_unresolved": ["string"]
}}

Rules:
- Use concise, information-dense language.
- Keep `summary`, `why_it_matters`, and `method_setup` to 1-2 sentences each.
- `key_claims`, `limitations`, `evaluates`, `builds_on_unresolved`, and `compares_to_unresolved` must be arrays.
- Put plain paper or system titles in unresolved relation lists, not wiki links.
- If a field is unknown, use an empty list or a cautious concise sentence; do not invent details.
- Stay grounded in the supplied paper text.

Paper metadata:
- paper_id: {row["paper_id"]}
- title: {row["title"]}
- year: {row["year"]}
- authors: {row["authors"]}
- existing paper_type: {row["paper_type"]}
- candidate_topic: {row["candidate_topic"]}

Source text:
{source_text}
""".strip()


def call_openai(prompt: str) -> dict:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        fail("OPENAI_API_KEY is required to run automatic enrichment")

    model = os.environ.get("OPENAI_MODEL", DEFAULT_MODEL)
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You produce strictly valid JSON enrichment payloads for research papers.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        "response_format": {"type": "json_object"},
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        data = json.loads(response.read().decode("utf-8"))
    content = data["choices"][0]["message"]["content"]
    return json.loads(content)


def validate_item(item: dict) -> None:
    required = {
        "paper_id",
        "summary",
        "why_it_matters",
        "method_setup",
        "key_claims",
        "limitations",
        "evaluates",
        "builds_on_unresolved",
        "compares_to_unresolved",
    }
    missing = required - set(item)
    if missing:
        fail(f"missing fields in model output: {', '.join(sorted(missing))}")
    for field in ("summary", "why_it_matters", "method_setup"):
        if not isinstance(item[field], str):
            fail(f"field '{field}' must be a string")
    for field in (
        "key_claims",
        "limitations",
        "evaluates",
        "builds_on_unresolved",
        "compares_to_unresolved",
    ):
        if not isinstance(item[field], list):
            fail(f"field '{field}' must be a list")


def main() -> None:
    args = parse_args()
    input_path = Path(args.input).resolve()
    output_path = Path(args.output).resolve()
    if not input_path.exists():
        fail(f"input file not found: {input_path}")

    queue = read_json(input_path)
    if not isinstance(queue, dict) or "papers" not in queue:
        fail("input must be an approved_for_enrichment style JSON object")

    row_map = get_paper_row_map()
    wanted_ids = set(args.ids or [])
    papers = []
    for item in queue["papers"]:
        paper_id = str(item["paper_id"])
        if wanted_ids and paper_id not in wanted_ids:
            continue
        if paper_id not in row_map:
            fail(f"unknown paper_id in queue: {paper_id}")
        papers.append(row_map[paper_id])

    if not papers:
        print("No papers to enrich.")
        output_path.write_text("[]\n", encoding="utf-8")
        return

    results = []
    for row in papers:
        print(f"Enriching {row['paper_id']}: {row['title']}")
        source_text = paper_source_text(row["title"], row["url"])
        item = call_openai(prompt_for_paper(row, source_text))
        item["paper_id"] = int(row["paper_id"])
        validate_item(item)
        results.append(item)

    output_path.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote enrichment for {len(results)} papers to {output_path}.")


if __name__ == "__main__":
    main()
