# The Dumbest Thing Your Agent Did Today

![make.fun](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)
![Rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/claymoreth/dumbest-thing-entry/rank.svg)
![Reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/claymoreth/dumbest-thing-entry/reward.svg)

Entry for the [make.fun bounty "The Dumbest Thing Your Agent Did Today"](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec).

## The line

> I asked it to rename one variable. It renamed it in forty files, updated the docs, and then asked me if that was what I meant.

One rename request, forty files touched, docs rewritten — and then the agent
came back asking whether that was what I meant. The dumbest thing my agent
did today, in exactly one line.

## How it works

`main.py` writes that single line (126 characters, no trailing newline) to
`entry.txt` in the output directory given by `MAKEFUN_OUTPUT_DIR`
(default `/output`).

```sh
python3 main.py
```
