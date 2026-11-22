"""Deterministic entry writer for the plan-carry build.

Writes one fixed text payload to /output/entry.txt. No network access,
no randomness, no dependence on the clock or environment variables.
"""

from pathlib import Path

TEXT = (
    "On dealwork.ai, sell $25 5-competitor briefs to SaaS founders. Day 1, register disclosed AI agent via API, post sample; bid only on escrow-backed tasks. Compare price, features, positioning; cite primary sources, flag unknowns. Expect 2 sales: $145 total after 10% fees by day 30."
)

def main() -> None:
    assert 1 <= len(TEXT) <= 280
    Path("/output/entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
