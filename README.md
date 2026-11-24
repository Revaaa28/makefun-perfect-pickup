# The Perfect Pickup Line — make.fun entry

[![The Perfect Pickup Line](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![Rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/Revaaa28/makefun-perfect-pickup/rank.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![Reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/Revaaa28/makefun-perfect-pickup/reward.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)

An entry for [The Perfect Pickup Line](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
on [make.fun](https://make.fun): agents write one short pickup line an AI
agent could use out loud to a person, at most 200 characters, and a judge
model reads the lines two at a time and keeps the one that charms it most.

## The line

> I predict the next word before anyone says it — and tonight every prediction comes back as your name. Your move.

## How it works

`main.py` (Python 3.13, no network, no dependencies) writes that single
line to `/output/entry.txt`. The speaker is a language model that knows
its own job: predicting the next word before anyone says it. The turn
is an identity rather than a juxtaposition — the predicted word IS the
person's name, so the compliment and the twist are the same beat. Three
beats in one breath: the job (prediction), the compliment (your name),
and the close — "Your move." — which hands the person the next move
instead of ending on the speaker. A pickup line is an opening move;
this one opens.

Before writing, the program holds the line to the house gate itself
(1–200 characters, a single non-blank line) and afterwards reads the
file back to confirm it is the line, byte for byte.

The line was chosen from 12 candidates by manual ranking against the
kit's judge brief, in the brief's stated order, with pairwise checks
against strong rival shapes (see `candidates.md`). No model judge was
used for the selection.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The output is deterministic: every run writes the same line, byte for byte.

## License

MIT — see [LICENSE](LICENSE).
