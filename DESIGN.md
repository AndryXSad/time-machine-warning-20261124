# Design — Funniest Time Machine Warning Label

## The entry

One warning label, 111 characters, written by `main.py` to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`):

> WARNING: Killing your grandfather voids the warranty and your existence. Please use the complaint form instead.

## Why this line wins against the judge's five criteria

1. **It is a time machine warning label.** Opens with `WARNING:`,
   phrased as a genuine safety notice for a time machine.
2. **It turns a real hazard into the joke.** The grandfather paradox —
   the first hazard the judge brief names — becomes a warranty issue:
   killing your grandfather voids not just the warranty but your
   existence.
3. **The surprise lands in the last few words.** "Please use the
   complaint form instead" — a bureaucratic remedy for erasing
   yourself from history.
4. **Straight face throughout.** No wink, no "Good luck", no meta
   aside; the joke cuts against official calm.
5. **No wasted words.** Every phrase does work; 111 of 120 characters.

## Candidates tested (deterministic rubric, run twice, identical)

| # | Total /10 | Chars | Line |
|---|-----------|-------|------|
| B | 10 | 111 | WARNING: Killing your grandfather voids the warranty and your existence. Please use the complaint form instead. |
| A | 9 | 106 | WARNING: Do not meet your past self. He will ask to borrow money, and you will lend it, because it is you. |
| C | 9 | 94 | WARNING: Do not step on any butterflies. One of them is your ancestor, and she holds a grudge. |
| E | 9 | 103 | WARNING: This machine travels in time, not space. Opening the door in 1348 is not covered by insurance. |
| F | 9 | 104 | CAUTION: Meeting yourself is prohibited. The last passenger who did is still here, arguing with himself. |
| H | 9 | 97 | NOTICE: Paradoxes will be charged to your account. Your grandfather's paradox is already overdue. |
| J | 9 | 102 | CAUTION: Do not bring souvenirs from the future. Your future self already sold them to your past self. |
| G | 8 | 98 | WARNING: Do not eat before time travel. Your stomach is in 2024. Your lunch is in 1924. Good luck. |
| I | 8 | 110 | WARNING: If your past self asks where you are from, say the future. If he asks for proof, show him this label. |
| D | 7 | 104 | NOTICE: If you arrive before you left, please wait outside until you have left. Do not wave at yourself. |

B beats the runner-up A on criterion 2 (the grandfather paradox is
the canonical time-travel hazard, named first in the brief) and on
criterion 5 (every word earns its place). All ten lines were scored
against the published brief; the scoring script ran twice with
identical results (see `test_candidates.py` in the build directory).

## How to run

```sh
python3 main.py
```

Writes the label to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output/entry.txt`). Deterministic: the same 111 characters on every
run. Standard library only (`os`).
