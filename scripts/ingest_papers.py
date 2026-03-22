#!/usr/bin/env python3

import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "paper_inbox" / "papers.csv"
ENRICHMENT_DIR = ROOT / "paper_inbox" / "enrichment"
NOTES_DIR = ROOT / "paper_notes"
TOPICS_DIR = ROOT / "topic_maps"
GENERATED_START = "<!-- GENERATED:START -->"
GENERATED_END = "<!-- GENERATED:END -->"
USER_FRONTMATTER_DEFAULTS = {
    "priority": "0",
    "last_read": "",
}
USER_OWNED_FIELDS = {"status", "priority", "last_read"}

REQUIRED_COLUMNS = [
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

ALLOWED_TOPICS = {
    "llm-multi-agent-systems": "LLM-Multi-Agent-Systems.md",
    "agent-evaluation": "Agent-Evaluation.md",
    "agent-harnesses": "Agent-Harnesses.md",
    "task-allocation": "Task-Allocation.md",
    "search-retrieval": "Search-Retrieval.md",
    "hallucination-factuality": "Hallucination-Factuality.md",
    "software-agents": "Software-Agents.md",
    "memory-context": "Memory-Context.md",
}

ALLOWED_TYPES = {"survey", "benchmark", "system", "position", "application"}
ALLOWED_STATUS = {
    "candidate",
    "approved",
    "ingested",
    "skimmed",
    "deep_read",
    "cited",
    "discarded",
}
ALLOWED_ENRICHMENT_STATUS = {"pending", "enriched", "failed"}
ACTIVE_NOTE_STATUS = {"approved", "ingested", "skimmed", "deep_read", "cited"}
ENRICHMENT_KEYS = {
    "summary": "",
    "why_it_matters": "",
    "method_setup": "",
    "key_claims": [],
    "limitations": [],
    "evaluates": [],
    "builds_on_unresolved": [],
    "compares_to_unresolved": [],
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def slug_title(title: str) -> str:
    cleaned = re.sub(r"[^\w\s-]", "", title).strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    words = cleaned.split()
    short = "-".join(words[:8]).strip("-")
    return short or "Untitled"


def note_name(year: str, title: str) -> str:
    return f"{year}-{slug_title(title)}.md"


def topic_link(topic_id: str) -> str:
    return ALLOWED_TOPICS[topic_id].replace(".md", "")


def normalize_title(value: str) -> str:
    cleaned = re.sub(r"[^\w\s-]", " ", value.strip().lower())
    return re.sub(r"\s+", " ", cleaned).strip()


def yaml_list_block(items: list[str]) -> str:
    if not items:
        return " []"
    lines = [""] 
    for item in items:
        lines.append(f"  - {yaml_string(item)}")
    return "\n".join(lines)


def yaml_string(value: str) -> str:
    return json.dumps(value)


def bullet_list(items: list[str]) -> str:
    if not items:
        return ""
    return "\n".join(f"- {item}" for item in items)


def load_enrichment(paper_id: str) -> dict:
    path = ENRICHMENT_DIR / f"{paper_id}.json"
    data = {key: value[:] if isinstance(value, list) else value for key, value in ENRICHMENT_KEYS.items()}
    if not path.exists():
        return data
    loaded = json.loads(path.read_text(encoding="utf-8"))
    for key in ENRICHMENT_KEYS:
        if key not in loaded:
            continue
        data[key] = loaded[key]
    return data


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}

    data: dict[str, str] = {}
    for line in parts[1].splitlines():
        if not line or line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def extract_user_notes(text: str) -> str:
    if not text:
        return ""
    if GENERATED_END in text:
        _, _, remainder = text.partition(GENERATED_END)
        remainder = remainder.lstrip("\n")
        if remainder.startswith("## My Notes"):
            _, _, notes = remainder.partition("\n")
            return notes.lstrip("\n").rstrip()
        return remainder.rstrip()
    if "\n## My Notes\n" in text:
        _, _, notes = text.partition("\n## My Notes\n")
        return notes.rstrip()
    return ""


def load_existing_note_state(path: Path, fallback_status: str) -> dict[str, str]:
    if not path.exists():
        return {
            "status": fallback_status,
            "priority": USER_FRONTMATTER_DEFAULTS["priority"],
            "last_read": USER_FRONTMATTER_DEFAULTS["last_read"],
            "my_notes": "",
        }

    text = path.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)
    return {
        "status": frontmatter.get("status", fallback_status),
        "priority": frontmatter.get("priority", USER_FRONTMATTER_DEFAULTS["priority"]),
        "last_read": frontmatter.get("last_read", USER_FRONTMATTER_DEFAULTS["last_read"]),
        "my_notes": extract_user_notes(text),
    }


def has_enrichment_file(paper_id: str) -> bool:
    return (ENRICHMENT_DIR / f"{paper_id}.json").exists()


def resolve_relations(
    unresolved_titles: list[str],
    title_index: dict[str, str],
) -> tuple[list[str], list[str]]:
    resolved: list[str] = []
    unresolved: list[str] = []
    for title in unresolved_titles:
        normalized = normalize_title(title)
        if normalized in title_index:
            resolved.append(f"[[{title_index[normalized]}]]")
        else:
            unresolved.append(title)
    return resolved, unresolved


def render_note(row: dict, title_index: dict[str, str], note_state: dict[str, str]) -> str:
    topic = topic_link(row["candidate_topic"])
    enrichment = load_enrichment(row["paper_id"])
    builds_on, builds_on_unresolved = resolve_relations(
        enrichment["builds_on_unresolved"], title_index
    )
    compares_to, compares_to_unresolved = resolve_relations(
        enrichment["compares_to_unresolved"], title_index
    )
    key_claims = bullet_list(enrichment["key_claims"])
    limitations = bullet_list(enrichment["limitations"])
    connections = [f"- [[{topic}]]"]
    for relation_type, values in (
        ("evaluates", enrichment["evaluates"]),
        ("builds_on", builds_on),
        ("compares_to", compares_to),
    ):
        for value in values:
            connections.append(f"- `{relation_type}` {value}")
    for relation_type, values in (
        ("builds_on_unresolved", builds_on_unresolved),
        ("compares_to_unresolved", compares_to_unresolved),
    ):
        for value in values:
            connections.append(f"- `{relation_type}` {value}")
    generated_block = f"""# Summary
{enrichment["summary"]}

# Why It Matters
{enrichment["why_it_matters"]}

# Method / Setup
{enrichment["method_setup"]}

# Key Claims
{key_claims}

# Limitations
{limitations}

# Connections
{chr(10).join(connections)}"""
    user_notes = note_state["my_notes"]
    my_notes_block = "## My Notes"
    if user_notes:
        my_notes_block += f"\n{user_notes}"
    else:
        my_notes_block += "\n"

    return f"""---
paper_id: {row["paper_id"]}
title: {yaml_string(row["title"])}
year: {row["year"]}
authors: {yaml_string(row["authors"])}
url: {yaml_string(row["url"])}
paper_type: {yaml_string(row["paper_type"])}
primary_topic: {yaml_string(row["candidate_topic"])}
secondary_topics: []
status: {yaml_string(note_state["status"])}
priority: {yaml_string(note_state["priority"])}
last_read: {yaml_string(note_state["last_read"])}
enrichment_status: {yaml_string(row["enrichment_status"])}
tags:
  - "papers"
  - {yaml_string(row["candidate_topic"])}
evaluates:{yaml_list_block(enrichment["evaluates"])}
builds_on:{yaml_list_block(builds_on)}
compares_to:{yaml_list_block(compares_to)}
builds_on_unresolved:{yaml_list_block(builds_on_unresolved)}
compares_to_unresolved:{yaml_list_block(compares_to_unresolved)}
relations: []
source: {yaml_string(row["source"])}
---
{GENERATED_START}
{generated_block}
{GENERATED_END}

{my_notes_block}
"""


def validate_row(row_num: int, row: dict) -> None:
    for key in REQUIRED_COLUMNS:
        if not row.get(key, "").strip():
            fail(f"row {row_num}: missing value for '{key}'")
    if row["candidate_topic"] not in ALLOWED_TOPICS:
        fail(f"row {row_num}: invalid candidate_topic '{row['candidate_topic']}'")
    if row["paper_type"] not in ALLOWED_TYPES:
        fail(f"row {row_num}: invalid paper_type '{row['paper_type']}'")
    if row["status"] not in ALLOWED_STATUS:
        fail(f"row {row_num}: invalid status '{row['status']}'")
    if row["enrichment_status"] not in ALLOWED_ENRICHMENT_STATUS:
        fail(
            f"row {row_num}: invalid enrichment_status "
            f"'{row['enrichment_status']}'"
        )
    if not row["paper_id"].isdigit():
        fail(f"row {row_num}: paper_id must be numeric")
    if not row["year"].isdigit() or len(row["year"]) != 4:
        fail(f"row {row_num}: year must be a 4-digit number")
    if not (row["url"].startswith("http://") or row["url"].startswith("https://")):
        fail(f"row {row_num}: url must start with http:// or https://")


def validate_duplicates(rows: list[dict]) -> None:
    seen_ids: set[str] = set()
    seen_titles: dict[str, str] = {}
    seen_urls: dict[str, str] = {}
    for row in rows:
        if row["paper_id"] in seen_ids:
            fail(f"duplicate paper_id '{row['paper_id']}'")
        seen_ids.add(row["paper_id"])

        norm_title = re.sub(r"\s+", " ", row["title"].strip().lower())
        if norm_title in seen_titles:
            fail(
                f"duplicate title between paper_id {seen_titles[norm_title]} "
                f"and {row['paper_id']}"
            )
        seen_titles[norm_title] = row["paper_id"]

        norm_url = row["url"].strip().lower().rstrip("/")
        if norm_url in seen_urls:
            fail(
                f"duplicate url between paper_id {seen_urls[norm_url]} "
                f"and {row['paper_id']}"
            )
        seen_urls[norm_url] = row["paper_id"]


def update_topic_maps(rows: list[dict]) -> None:
    grouped: dict[str, list[str]] = {topic: [] for topic in ALLOWED_TOPICS}
    for row in rows:
        if row["status"] not in {"ingested", "skimmed", "deep_read", "cited"}:
            continue
        grouped[row["candidate_topic"]].append(
            f"- [[{note_name(row['year'], row['title']).replace('.md', '')}]]"
        )

    for topic_id, filename in ALLOWED_TOPICS.items():
        path = TOPICS_DIR / filename
        content = path.read_text()
        head, _, _ = content.partition("## Included Papers")
        entries = "\n".join(grouped[topic_id]).strip()
        if entries:
            updated = f"{head}## Included Papers\n\n{entries}\n"
        else:
            updated = f"{head}## Included Papers\n"
        path.write_text(updated)


def main() -> None:
    if not INBOX.exists():
        fail(f"missing inbox file: {INBOX}")

    with INBOX.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != REQUIRED_COLUMNS:
            fail(
                "papers.csv header must exactly match: "
                + ",".join(REQUIRED_COLUMNS)
            )
        rows = list(reader)

    for idx, row in enumerate(rows, start=2):
        validate_row(idx, row)
    validate_duplicates(rows)

    rendered_count = 0
    newly_ingested_count = 0
    note_states: dict[str, dict[str, str]] = {}
    effective_rows: list[dict] = []
    for row in rows:
        filename = note_name(row["year"], row["title"])
        path = NOTES_DIR / filename
        initial_status = "ingested" if row["status"] == "approved" else row["status"]
        note_state = load_existing_note_state(path, initial_status)
        note_states[row["paper_id"]] = note_state

        effective_row = dict(row)
        effective_row["status"] = note_state["status"]
        if row["status"] == "approved" and note_state["status"] == "ingested":
            newly_ingested_count += 1
        effective_rows.append(effective_row)

    title_index = {
        normalize_title(row["title"]): note_name(row["year"], row["title"]).replace(".md", "")
        for row in effective_rows
        if row["status"] in ACTIVE_NOTE_STATUS
    }
    for row, effective_row in zip(rows, effective_rows):
        row["status"] = effective_row["status"]
        if row["status"] not in ACTIVE_NOTE_STATUS:
            continue
        if not has_enrichment_file(row["paper_id"]) and row["enrichment_status"] != "failed":
            row["enrichment_status"] = "pending"
        filename = note_name(row["year"], row["title"])
        path = NOTES_DIR / filename
        path.write_text(
            render_note(row, title_index, note_states[row["paper_id"]]),
            encoding="utf-8",
        )
        rendered_count += 1

    with INBOX.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=REQUIRED_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    update_topic_maps(rows)
    print(
        f"Rendered {rendered_count} active notes; "
        f"newly ingested {newly_ingested_count} approved papers."
    )


if __name__ == "__main__":
    main()
