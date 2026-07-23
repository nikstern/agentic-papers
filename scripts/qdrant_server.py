#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request


DEFAULT_URL = "http://127.0.0.1:6333"


def server_url() -> str:
    return os.environ.get("QDRANT_URL", DEFAULT_URL).rstrip("/")


def ready(url: str, timeout: float = 2.0) -> bool:
    try:
        with urllib.request.urlopen(f"{url}/readyz", timeout=timeout) as response:
            return response.status == 200
    except (urllib.error.URLError, TimeoutError):
        return False


def wait_until_ready(url: str, timeout: float) -> bool:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if ready(url):
            return True
        time.sleep(1)
    return ready(url)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check the local Qdrant server.")
    parser.add_argument("command", choices=("status", "wait"))
    parser.add_argument("--timeout", type=float, default=60.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    url = server_url()
    is_ready = (
        wait_until_ready(url, args.timeout)
        if args.command == "wait"
        else ready(url)
    )
    print(json.dumps({"url": url, "ready": is_ready}))
    if not is_ready:
        print(
            "Qdrant is not ready. Start it with `make search-server-up`.",
            file=sys.stderr,
        )
        raise SystemExit(1)


if __name__ == "__main__":
    main()
