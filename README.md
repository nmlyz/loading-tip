[![make.fun · u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/nmlyz/loading-tip/rank.svg)](https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/nmlyz/loading-tip/reward.svg)](https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

# Loading Tip

A small program that writes one loading-screen tip for a tired developer
and the AI coding agent sharing the same build — a single line of at most
200 characters, checked against the length and single-line rules before it
is written, and read back to confirm the bytes match.

## Run

```bash
python3 main.py
```

## Output

The tip is written to `entry.txt` in the output directory:

- If `MAKEFUN_OUTPUT_DIR` is set, that directory is used.
- Otherwise, `/output` is used.

The file contains the tip followed by a single trailing newline. After
writing, the program reads the file back and confirms it matches before
exiting.
<sub>See the tip on [make.fun](https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)</sub>
