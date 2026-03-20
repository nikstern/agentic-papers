#!/usr/bin/env python3

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SEARCH_INDEXER = ROOT / "search" / "index_qdrant.py"
VENV_PYTHON = ROOT / ".venv" / "bin" / "python"


def main() -> None:
    if not SEARCH_INDEXER.exists():
        print("Search reindex skipped: search/index_qdrant.py not found.")
        return

    if not VENV_PYTHON.exists():
        print("Search reindex skipped: .venv is missing. Run `python3 -m venv .venv` and install search dependencies.")
        return

    print("Refreshing Qdrant search index...")
    result = subprocess.run(
        [str(VENV_PYTHON), str(SEARCH_INDEXER)],
        cwd=ROOT,
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
