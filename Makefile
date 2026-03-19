ingest:
	python3 scripts/ingest_papers.py

approve:
	@test -n "$(IDS)" || (echo "Usage: make approve IDS='1 2 3'" && exit 1)
	python3 scripts/approve_papers.py $(IDS)

import-candidates:
	@test -n "$(FILE)" || (echo "Usage: make import-candidates FILE=paper_inbox/mcp_candidates.example.json" && exit 1)
	python3 scripts/import_mcp_candidates.py $(FILE)

import-enrichment:
	@test -n "$(FILE)" || (echo "Usage: make import-enrichment FILE=paper_inbox/enrichment.example.json" && exit 1)
	python3 scripts/import_enrichment.py $(FILE)

export-enrichment-input:
	python3 scripts/export_enrichment_input.py

rank-papers:
	python3 scripts/rank_papers.py $(ARGS)

email-reading-queue:
	python3 scripts/email_reading_queue.py $(ARGS)

mark-enrichment-failed:
	@test -n "$(IDS)" || (echo "Usage: make mark-enrichment-failed IDS='1 2 3'" && exit 1)
	python3 scripts/mark_enrichment_failed.py $(IDS)
