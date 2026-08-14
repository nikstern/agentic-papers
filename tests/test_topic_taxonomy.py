from __future__ import annotations

from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import import_mcp_candidates
import ingest_papers
import rank_papers


class TopicTaxonomyTests(unittest.TestCase):
    def test_multi_agent_foundations_is_supported_consistently(self) -> None:
        topic = "multi-agent-foundations"

        self.assertIn(topic, import_mcp_candidates.ALLOWED_TOPICS)
        self.assertEqual(
            ingest_papers.ALLOWED_TOPICS[topic],
            "Multi-Agent-Foundations.md",
        )
        self.assertEqual(rank_papers.TOPIC_WEIGHTS[topic], 3.0)

    def test_multi_agent_foundations_map_has_generated_section(self) -> None:
        path = ROOT / "topic_maps" / "Multi-Agent-Foundations.md"
        content = path.read_text(encoding="utf-8")

        self.assertIn("topic_id: multi-agent-foundations", content)
        self.assertIn("## Scope", content)
        self.assertIn("## Included Papers", content)

    def test_medical_time_series_is_supported_consistently(self) -> None:
        topic = "medical-time-series"

        self.assertIn(topic, import_mcp_candidates.ALLOWED_TOPICS)
        self.assertEqual(
            ingest_papers.ALLOWED_TOPICS[topic],
            "Medical-Time-Series.md",
        )
        self.assertEqual(rank_papers.TOPIC_WEIGHTS[topic], 3.5)

    def test_medical_time_series_map_has_generated_section(self) -> None:
        path = ROOT / "topic_maps" / "Medical-Time-Series.md"
        content = path.read_text(encoding="utf-8")

        self.assertIn("topic_id: medical-time-series", content)
        self.assertIn("## Scope", content)
        self.assertIn("## Included Papers", content)


if __name__ == "__main__":
    unittest.main()
