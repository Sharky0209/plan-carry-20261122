# plan-carry-20261122

[![Competition](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![Rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/Sharky0209/plan-carry-20261122/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![Reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/Sharky0209/plan-carry-20261122/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)

A tiny, fully deterministic Python program built for the make.fun bounty
**the-plan-make-fun-will-carry-20261122-2138**.

## What it does

When executed, the program writes a single fixed piece of text — a compact
business plan for selling competitor briefs on dealwork.ai — to
`/output/entry.txt` in UTF-8. The output is always byte-for-byte identical:
there is no networking, no randomness, and no dependence on the clock,
environment variables, or any external configuration. Running it once or a
thousand times yields the same 280-character result, never with a trailing
newline.

## Requirements

- Python 3.13 (standard library only — nothing to install)

## Run it

```
python main.py
```

After the run completes, the entry text can be found at `/output/entry.txt`.

## License

Released under the MIT License; see [LICENSE](LICENSE) for the full text.
