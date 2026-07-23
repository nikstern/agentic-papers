from __future__ import annotations

import os
from pathlib import Path
from types import SimpleNamespace
import sys
import unittest
from unittest import mock


SEARCH_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SEARCH_DIR))

import common
import index_qdrant


class FakeClient:
    def __init__(self) -> None:
        self.collections: set[str] = set()
        self.aliases: dict[str, str] = {}
        self.counts: dict[str, int] = {}
        self.alias_updates = []

    def get_aliases(self):
        return SimpleNamespace(
            aliases=[
                SimpleNamespace(alias_name=alias, collection_name=collection)
                for alias, collection in self.aliases.items()
            ]
        )

    def collection_exists(self, name: str) -> bool:
        return name in self.collections or name in self.aliases

    def create_collection(self, collection_name: str, vectors_config) -> None:
        self.collections.add(collection_name)
        self.counts[collection_name] = 0

    def delete_collection(self, collection_name: str) -> None:
        self.collections.discard(collection_name)
        self.counts.pop(collection_name, None)

    def upsert(self, collection_name: str, points) -> None:
        self.counts[collection_name] = len(points)

    def count(self, collection_name: str, exact: bool):
        return SimpleNamespace(count=self.counts[collection_name])

    def update_collection_aliases(self, operations) -> bool:
        self.alias_updates.append(operations)
        for operation in operations:
            delete_alias = getattr(operation, "delete_alias", None)
            create_alias = getattr(operation, "create_alias", None)
            if delete_alias is not None:
                self.aliases.pop(delete_alias.alias_name, None)
            if create_alias is not None:
                self.aliases[create_alias.alias_name] = (
                    create_alias.collection_name
                )
        return True


class BackendConfigurationTests(unittest.TestCase):
    def test_server_is_default_and_uses_localhost(self) -> None:
        with mock.patch.dict(os.environ, {}, clear=True):
            with mock.patch.object(common, "QdrantClient") as client_class:
                common.get_client()

        client_class.assert_called_once_with(
            url="http://127.0.0.1:6333",
            api_key=None,
            timeout=5.0,
        )

    def test_embedded_mode_requires_explicit_opt_in(self) -> None:
        with mock.patch.dict(os.environ, {"QDRANT_MODE": "embedded"}, clear=True):
            with mock.patch.object(common, "QdrantClient") as client_class:
                common.get_client()

        client_class.assert_called_once_with(path=str(common.DEFAULT_LOCAL_PATH))

    def test_explicit_server_settings_override_defaults(self) -> None:
        environment = {
            "QDRANT_MODE": "server",
            "QDRANT_URL": "http://localhost:7000/",
            "QDRANT_API_KEY": "secret",
            "QDRANT_TIMEOUT": "9",
        }
        with mock.patch.dict(os.environ, environment, clear=True):
            with mock.patch.object(common, "QdrantClient") as client_class:
                common.get_client()

        client_class.assert_called_once_with(
            url="http://localhost:7000",
            api_key="secret",
            timeout=9.0,
        )

    def test_invalid_mode_and_timeout_are_rejected(self) -> None:
        with mock.patch.dict(os.environ, {"QDRANT_MODE": "automatic"}, clear=True):
            with self.assertRaisesRegex(ValueError, "QDRANT_MODE"):
                common.get_backend_mode()
        with mock.patch.dict(os.environ, {"QDRANT_TIMEOUT": "0"}, clear=True):
            with self.assertRaisesRegex(ValueError, "positive"):
                common.get_timeout()
        with mock.patch.dict(os.environ, {"QDRANT_URL": " "}, clear=True):
            with self.assertRaisesRegex(ValueError, "cannot be empty"):
                common.get_server_url()

    def test_unavailable_server_has_actionable_message(self) -> None:
        unavailable = mock.Mock()
        unavailable.get_collections.side_effect = OSError("offline")
        with mock.patch.dict(os.environ, {}, clear=True):
            with mock.patch.object(common, "get_client", return_value=unavailable):
                with self.assertRaisesRegex(
                    RuntimeError,
                    "make search-server-up",
                ):
                    common.require_client()


class AtomicPublishTests(unittest.TestCase):
    def test_alias_switch_replaces_complete_collection_and_removes_old(self) -> None:
        client = FakeClient()
        client.collections.add("agentic-papers__build_old")
        client.counts["agentic-papers__build_old"] = 1
        client.aliases["agentic-papers"] = "agentic-papers__build_old"

        published = index_qdrant.publish_server_collection(
            client,
            "agentic-papers",
            3,
            [object(), object()],
            build_id="new",
        )

        self.assertEqual(published, "agentic-papers__build_new")
        self.assertEqual(
            client.aliases["agentic-papers"],
            "agentic-papers__build_new",
        )
        self.assertNotIn("agentic-papers__build_old", client.collections)
        self.assertEqual(client.counts[published], 2)
        self.assertEqual(len(client.alias_updates), 1)
        self.assertEqual(len(client.alias_updates[0]), 2)

    def test_failed_validation_preserves_previous_alias(self) -> None:
        client = FakeClient()
        client.collections.add("agentic-papers__build_old")
        client.counts["agentic-papers__build_old"] = 1
        client.aliases["agentic-papers"] = "agentic-papers__build_old"

        def incorrect_count(collection_name: str, exact: bool):
            return SimpleNamespace(count=0)

        client.count = incorrect_count
        with self.assertRaisesRegex(RuntimeError, "validation failed"):
            index_qdrant.publish_server_collection(
                client,
                "agentic-papers",
                3,
                [object()],
                build_id="bad",
            )

        self.assertEqual(
            client.aliases["agentic-papers"],
            "agentic-papers__build_old",
        )
        self.assertNotIn("agentic-papers__build_bad", client.collections)

    def test_first_publish_replaces_legacy_physical_collection(self) -> None:
        client = FakeClient()
        client.collections.add("agentic-papers")
        client.counts["agentic-papers"] = 1

        index_qdrant.publish_server_collection(
            client,
            "agentic-papers",
            3,
            [object()],
            build_id="first",
        )

        self.assertNotIn("agentic-papers", client.collections)
        self.assertEqual(
            client.aliases["agentic-papers"],
            "agentic-papers__build_first",
        )


if __name__ == "__main__":
    unittest.main()
