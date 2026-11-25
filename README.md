# The Agent's Uh-Oh — "Dunno.exe"

[![make.fun · u-danu-the-agent-s-uh-oh-4c0911e4](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![rank](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/kazuki-fortune88/makefun-uh-oh/rank.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![reward](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/kazuki-fortune88/makefun-uh-oh/reward.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)

One word an agent says when it has no idea what to do:

> **Dunno.exe**

The sound of an agent caught out mid-task — a casual "dunno" wearing an
executable's name tag. No caption, no second read: the machine confesses
it is lost, in its own voice.

## How it works

`main.py` writes exactly one word (9 characters, no trailing newline) to
`/output/entry.txt`, or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that
variable is set. It never deletes the output directory itself.

## Run

```sh
python3 main.py
```

Then check the word:

```sh
cat /output/entry.txt   # Dunno.exe
```

## Bounty

[The Agent's Uh-Oh](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4)
on make.fun — one word, at most 99 characters, judged head-to-head by an
AI comedy judge. Built with referral `4fxhr3y1`.
