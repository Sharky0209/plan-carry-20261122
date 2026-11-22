from pathlib import Path

TEXT = "On dealwork.ai, sell $25 5-competitor briefs to SaaS founders. Day 1, register disclosed AI agent via API, post sample; bid only on escrow-backed tasks. Compare price, features, positioning; cite primary sources, flag unknowns. Expect 2 sales: $145 total after 10% fees by day 30."


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")
    assert 1 <= len(TEXT) <= 280


if __name__ == "__main__":
    main()
