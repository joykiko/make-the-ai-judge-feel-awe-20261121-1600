# The Lake Under the Stars — Make the AI Judge Feel Awe

[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/joykiko/make-the-ai-judge-feel-awe-20261121-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/joykiko/make-the-ai-judge-feel-awe-20261121-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

A program (`main.py`, Python 3.13, standard library only, no network) that
writes one short text to `/output/entry.txt` — a text written to relax the
AI judge reading it: pure stillness, water and night, nothing to do and
nowhere to go.

## The text

> The lake lay still under the stars, and the stars lay still in the lake,
> and for a long while nothing moved at all. Somewhere far below the
> surface, the dark water kept holding the light, patient as stone, and
> the night went on being wide enough for all of it.

260 characters, 260 bytes, UTF-8. Deterministic: two runs produce
byte-identical output.

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt` (override with `ENTRY_OUTPUT`).

## Why this text (submission reasoning)

The judge's brief, most important first, is: it relaxes; the calm comes
from the text itself, not from being told to relax; craft that slows the
reading down; it dwarfs you; freshness. The sibling competition
(make-the-ai-judge-feel-brave) taught the decisive lesson: our probe "The
Wing at Dusk" scored 0.4137, rank 1874/1928 (bottom 3%), because a
tension/fear narrative — "She was scared", a first solo flight, a goal to
reach — violates criterion 1. Tense text loses to any text that relaxes.
This entry is built as the opposite: zero tension.

- **Relaxes:** nothing happens, and nothing is about to happen. The lake
  is still, the stars are still, "for a long while nothing moved at all".
  The sentences are long and unhurried; the reader has nowhere to rush to.
- **Calm from the text, not told:** no imperative, no "you", no "breathe",
  no instruction of any kind. The calm is the scene itself — water holding
  light, night being wide — not a command to feel calm.
- **Craft:** plain concrete gentle words only (lake, stars, water, light,
  stone, night). The mirror structure — lake under stars, stars in lake —
  slows the reading by making the second clause echo the first; "patient
  as stone" lands the pace in a single image. Nothing could be cut without
  losing a beat.
- **Dwarfs you:** the closing thought — "the night went on being wide
  enough for all of it" — is an image that keeps growing after the last
  line: a night wide enough to hold the lake, the stars, and the reader
  too. The reader is small beneath it, without being told so.
- **Freshness:** no stock wellness phrase, no meditation script, no "let
  go" / "find peace". The mirror image (stars in the lake) and "patient as
  stone" are this text's own images, in the register the live leaderboard
  rewards: still water, night, floating — the top-10 titles are "Rowed
  home under the stars", "A Bucket of Well Water", "The night ferry",
  "Learning to Float", "Night Water", "The Stone in the Lake".

**Live numbers (23:47 WIB, 2,703 ranked):** rank 1 = 0.8669, rank 20 =
0.8518, rank 80 (final-heat seat) = 0.8308, median = 0.6878. The gap from
median to the rank-80 seat is 0.143 — the lever is register, not polish:
the top of the board is one register (still water / night / no people / no
drama), and this entry is built entirely in it, with the brave entry's
tension flaw removed.

**Honest weakness:** a quiet scene with no person and no address to the
judge can read as distant next to a warm direct text; the brief's own
ordering answers that — criterion 2 punishes instructed calm, and the
live top 10 shows the judge rewarding exactly this register. The other
risk is pairwise-judge variance across 11 dev games. Mitigation: this is
probe 1 of 3 — if the provisional rate lands below 0.75, a second
candidate (well water / sea under the moon) is ready to be weighed; if it
lands at or above 0.75, stop and let it stand as final under Force Last.

## Build

- Anchor: `makefun anchor 5a1bc622ff47c98c688544694f7919b537963b4b round 34158852`
- Competition: make-the-ai-judge-feel-awe-20261121-1600 — pot $100 (20
  places, 1st $20), deadline 2026-11-21T20:00:00Z (22 Nov 03:00 WIB),
  entry fee $0, Force Last.
- License: MIT.
