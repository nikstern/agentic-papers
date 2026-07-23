from __future__ import annotations

from typing import Any


REQUIRED_FIELDS = (
    "paper_id",
    "summary",
    "why_it_matters",
    "method_setup",
    "key_claims",
    "limitations",
    "evaluates",
    "builds_on_unresolved",
    "compares_to_unresolved",
)
TEXT_FIELDS = ("summary", "why_it_matters", "method_setup")
LIST_FIELDS = (
    "key_claims",
    "limitations",
    "evaluates",
    "builds_on_unresolved",
    "compares_to_unresolved",
)

ENRICHMENT_JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "paper_id": {"type": "integer"},
        **{field: {"type": "string"} for field in TEXT_FIELDS},
        **{
            field: {"type": "array", "items": {"type": "string"}}
            for field in LIST_FIELDS
        },
    },
    "required": list(REQUIRED_FIELDS),
    "additionalProperties": False,
}


class EnrichmentValidationError(ValueError):
    pass


def normalize_paper_id(value: Any) -> str:
    if isinstance(value, bool):
        raise EnrichmentValidationError("paper_id must be numeric")
    paper_id = str(value)
    if not paper_id.isdigit():
        raise EnrichmentValidationError("paper_id must be numeric")
    return paper_id


def validate_enrichment_item(
    item: Any,
    *,
    expected_paper_id: str | None = None,
    known_ids: set[str] | None = None,
) -> dict:
    if not isinstance(item, dict):
        raise EnrichmentValidationError("each enrichment item must be an object")

    missing = set(REQUIRED_FIELDS) - set(item)
    if missing:
        raise EnrichmentValidationError(
            f"missing fields: {', '.join(sorted(missing))}"
        )
    extras = set(item) - set(REQUIRED_FIELDS)
    if extras:
        raise EnrichmentValidationError(
            f"unexpected fields: {', '.join(sorted(extras))}"
        )

    paper_id = normalize_paper_id(item["paper_id"])
    if expected_paper_id is not None and paper_id != str(expected_paper_id):
        raise EnrichmentValidationError(
            f"paper_id {paper_id} does not match expected paper_id {expected_paper_id}"
        )
    if known_ids is not None and paper_id not in known_ids:
        raise EnrichmentValidationError(f"unknown paper_id '{paper_id}'")

    for field in TEXT_FIELDS:
        if not isinstance(item[field], str):
            raise EnrichmentValidationError(f"'{field}' must be a string")
    for field in LIST_FIELDS:
        value = item[field]
        if not isinstance(value, list):
            raise EnrichmentValidationError(f"'{field}' must be a list")
        if any(not isinstance(entry, str) for entry in value):
            raise EnrichmentValidationError(
                f"every entry in '{field}' must be a string"
            )

    normalized = {field: item[field] for field in REQUIRED_FIELDS}
    normalized["paper_id"] = paper_id
    return normalized
