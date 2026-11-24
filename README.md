# Funniest Time Machine Warning Label

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Entry: 86 chars](https://img.shields.io/badge/entry-86%20chars-brightgreen)](main.py)

Entry for the [make.fun bounty "Funniest Time Machine Warning Label"](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151) — a single warning label for a time machine, 120 characters at most, judged by an AI comedy headliner in head-to-head rounds.

## The entry

> **WARNING: The return trip departs five minutes before you arrive. Do not miss it twice.**

86 characters. The joke turns a real time-travel hazard — a return trip that leaves before you even arrive, stranding you — into a deadpan safety notice, and saves the punch for the very last word: *twice*.

## How it works

`main.py` is deterministic: no network, no randomness, no time dependence. It writes the label to `/output/entry.txt`.

```sh
python3 main.py
cat /output/entry.txt
```

## Why this line

The field is flooded with "do not meet yourself" and "do not kill your grandfather" variants. This line takes a fresh hazard (missing a return departure that already happened), keeps a straight official face, and lands the surprise at the end — the three things the judge brief weighs most. Full candidate list and three review rounds: see `../REVIEW.md`.

## License

MIT — see [LICENSE](LICENSE).
