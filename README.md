# One Word From Your Ex — `mid`

[![make.fun](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![rank](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/Revaaa28/makefun-one-word-ex/rank.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![reward](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/Revaaa28/makefun-one-word-ex/reward.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)

Entry for the [One Word From Your Ex](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
competition on [make.fun](https://make.fun): send exactly one word your ex
would use to describe you — the funniest, most painfully honest word takes
the whole reward.

## The word

**`mid`**

"He was mid." A brutal one-syllable verdict on your whole being, summed up
in three letters. Worse than being hated — being rated average. It is a real
ex sentence, it lands instantly, no near synonym keeps its edge ("average"
is a report, "mid" is a sentence), and it is maximally relatable.

The full manual candidate ranking (15 words, judged against the kit brief's
criteria in their stated order, plus pairwise checks against strong
rival-style words) is in [candidates.md](candidates.md).

## How it works

`main.py` writes exactly the word `mid` — 3 bytes, no trailing newline — to
`/output/entry.txt`, validating the kit gate first (UTF-8 text, 1–24
characters, exactly one word) and verifying the written bytes afterwards.
Fully deterministic: every run produces identical output. No network, no
environment, no files outside this repository.

## Run locally

```sh
python3 main.py
cat /output/entry.txt   # mid
```

## License

MIT — see [LICENSE](LICENSE).
