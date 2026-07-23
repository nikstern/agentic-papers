ingest:
	python3 scripts/ingest_papers.py
	python3 scripts/export_enrichment_input.py
	python3 scripts/reindex_search.py

approve:
	@test -n "$(IDS)" || (echo "Usage: make approve IDS='1 2 3'" && exit 1)
	python3 scripts/approve_papers.py $(IDS)

import-candidates:
	@test -n "$(FILE)" || (echo "Usage: make import-candidates FILE=paper_inbox/mcp_candidates.example.json" && exit 1)
	python3 scripts/import_mcp_candidates.py $(FILE)

import-enrichment:
	@test -n "$(FILE)" || (echo "Usage: make import-enrichment FILE=paper_inbox/enrichment.example.json" && exit 1)
	python3 scripts/import_enrichment.py $(FILE)
	$(MAKE) ingest

export-enrichment-input:
	python3 scripts/export_enrichment_input.py

enrich-pending:
	$(MAKE) export-enrichment-input
	python3 scripts/run_enrichment.py
	$(MAKE) import-enrichment FILE=paper_inbox/auto_enrichment_output.json

ingest-and-enrich:
	$(MAKE) ingest
	$(MAKE) enrich-pending

rank-papers:
	python3 scripts/rank_papers.py $(ARGS)

email-reading-queue:
	python3 scripts/email_reading_queue.py $(ARGS)

mark-enrichment-failed:
	@test -n "$(IDS)" || (echo "Usage: make mark-enrichment-failed IDS='1 2 3'" && exit 1)
	python3 scripts/mark_enrichment_failed.py $(IDS)

test:
	python3 -m unittest discover -s tests -p 'test_*.py' -v
