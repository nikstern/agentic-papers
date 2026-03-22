#!/usr/bin/env python3

import argparse
import html
import subprocess
import sys
from datetime import date
from pathlib import Path

from rank_papers import (
    ACTIVE_READING_STATUSES,
    compute_scores,
    load_enrichment,
    load_rows,
    load_topic_weights,
)


GMAIL_HELPER = Path("/Users/nikstern/.local/bin/codex-send-gmail")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Email the current ranked reading queue through Gmail."
    )
    parser.add_argument("--top", type=int, default=5, help="number of papers to include")
    parser.add_argument(
        "--status",
        action="append",
        dest="statuses",
        help="include only these statuses; defaults to active reading statuses",
    )
    parser.add_argument(
        "--topic-weight-file",
        help="optional JSON file overriding topic weights",
    )
    parser.add_argument(
        "--subject",
        help="optional email subject override",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the email body instead of sending it",
    )
    return parser.parse_args()


def format_text(ranked: list[dict]) -> str:
    lines = [
        "Papers to read next:",
        "",
    ]
    for index, item in enumerate(ranked, start=1):
        reasons = describe_reasons(item)
        enrichment = enrichment_snippets(item)
        lines.append(f"{index}. [Vault ID {item['paper_id']}] {item['title']} ({item['year']})")
        lines.append(f"   {display_label(item)}")
        for reason in reasons:
            lines.append(f"   - {reason}")
        for snippet in enrichment:
            lines.append(f"   - {snippet}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def format_html(ranked: list[dict]) -> str:
    items = []
    for item in ranked:
        reasons = describe_reasons(item)
        enrichment = enrichment_snippets(item)
        title = html.escape(item["title"])
        url = html.escape(item["url"])
        label = html.escape(display_label(item))
        vault_id = html.escape(str(item["paper_id"]))
        reason_items = "".join(f"<li>{html.escape(reason)}</li>" for reason in reasons)
        enrichment_items = "".join(
            f"<li>{html.escape(snippet)}</li>" for snippet in enrichment
        )
        items.append(
            "<li>"
            f"<p><strong>Vault ID {vault_id}</strong><br>"
            f"<a href=\"{url}\"><strong>{title}</strong></a> ({item['year']})</p>"
            f"<p>{label}</p>"
            f"<ul>{reason_items}{enrichment_items}</ul>"
            "</li>"
        )
    return (
        "<p>Papers to read next:</p>"
        f"<ol>{''.join(items)}</ol>"
    )


def build_subject(override: str | None) -> str:
    if override:
        return override
    return f"Reading queue for {date.today().isoformat()}"


def topic_label(topic: str) -> str:
    return topic.replace("-", " ").title()


def type_label(paper_type: str) -> str:
    return paper_type.replace("-", " ").title()


def display_label(item: dict) -> str:
    return f"{topic_label(item['candidate_topic'])} {type_label(item['paper_type'])}"


def describe_reasons(item: dict) -> list[str]:
    reasons: list[str] = []
    components = item["components"]
    priority_value = str(item.get("priority", "")).strip()

    if components["priority"] > 0:
        reasons.append("manually prioritized")
    if components["topic_fit"] >= 4.0:
        reasons.append("high-priority topic")
    if item["paper_type"] == "survey":
        reasons.append("survey for orientation")
    elif item["paper_type"] == "benchmark":
        reasons.append("benchmark for evaluation coverage")
    elif item["paper_type"] == "position":
        reasons.append("position paper for framing")
    elif item["paper_type"] == "system":
        reasons.append("system paper for implementation detail")
    if components["foundation_bonus"] > 0:
        reasons.append("foundational paper in this topic")
    if components["centrality"] >= 1.5:
        reasons.append("heavily referenced in the vault")
    elif components["centrality"] > 0:
        reasons.append("referenced by related papers")
    if components["gap_bonus"] >= 1.25:
        reasons.append("fills a topic gap")
    if components["recency"] >= 1.25:
        reasons.append("recent work")

    if not reasons and priority_value:
        reasons.append("manually triaged")
    if not reasons:
        reasons.append("ranked highly by the current reading model")
    return reasons[:3]


def compact_sentence(value: str, limit: int = 220) -> str:
    compact = " ".join(str(value).split())
    if len(compact) <= limit:
        return compact
    return compact[: limit - 3] + "..."


def enrichment_snippets(item: dict) -> list[str]:
    enrichment = load_enrichment(str(item["paper_id"]))
    snippets: list[str] = []

    why = str(enrichment.get("why_it_matters", "")).strip()
    if why:
        snippets.append(f"Why it matters: {compact_sentence(why)}")

    key_claims = enrichment.get("key_claims", [])
    if isinstance(key_claims, list) and key_claims:
        snippets.append(f"Key claim: {compact_sentence(str(key_claims[0]))}")
    else:
        setup = str(enrichment.get("method_setup", "")).strip()
        if setup:
            snippets.append(f"Setup: {compact_sentence(setup)}")

    limitations = enrichment.get("limitations", [])
    if isinstance(limitations, list) and limitations:
        snippets.append(f"Limitation: {compact_sentence(str(limitations[0]))}")

    return snippets[:3]


def send_email(subject: str, text_body: str, html_body: str) -> None:
    if not GMAIL_HELPER.exists():
        fail(f"Gmail helper not found: {GMAIL_HELPER}")
    subprocess.run(
        [
            str(GMAIL_HELPER),
            "--subject",
            subject,
            "--text",
            text_body,
            "--html",
            html_body,
        ],
        check=True,
    )


def main() -> None:
    args = parse_args()
    rows = load_rows()
    statuses = set(args.statuses or ACTIVE_READING_STATUSES)
    topic_weights = load_topic_weights(args.topic_weight_file)
    ranked = compute_scores(rows, statuses, topic_weights)[: args.top]
    if not ranked:
        fail("no papers matched the requested statuses")

    subject = build_subject(args.subject)
    text_body = format_text(ranked)
    html_body = format_html(ranked)

    if args.dry_run:
        print(f"Subject: {subject}\n")
        print(text_body, end="")
        return

    send_email(subject, text_body, html_body)


if __name__ == "__main__":
    main()
