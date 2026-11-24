[![make.fun · u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![rank](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/giandisruw/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![reward](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/giandisruw/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)

# The Long Roast: Lawmakers and the File They Cannot Convert

Entry for the make.fun bounty [The Long Roast: Lawmakers and the File They Cannot Convert](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7) — one satirical sentence, at most 320 characters, roasting lawmakers who would regulate AI, crypto or the internet but cannot convert a file to PDF.

## The line

**The senator drafting the law to audit every algorithm on Earth just asked his intern to print the internet so he can convert it to PDF by hand.**

Character count: **143** (limit: 320).

## How it works

`main.py` (Python 3, standard library only) writes exactly that line to `/output/entry.txt` — no trailing newline, nothing else. Before writing, it validates the line: 1–320 characters, a single line, no leading or trailing whitespace, no control characters. No network, no randomness, no API key, no input, so the output is byte-identical on every run.

```bash
python3 main.py
```

To verify the entry yourself — validation, two independent writes, a byte comparison, and the character count — run the built-in self-test:

```bash
python3 main.py --self-test
```

It prints the line, its character count, a PASS/FAIL verdict for each check, and exits 0 only if every check passes. It writes only to a fresh temporary directory and leaves `/output/entry.txt` untouched.

## Why it is funny

A senator sets out to audit every algorithm on Earth — the grandest possible regulatory ambition — and is immediately undercut by needing his intern to print the internet so he can convert it to PDF by hand. "By hand" is the punch: converting a file to PDF is a two-click job, and doing it by hand is absurd. The setup is about the rules he writes (a law to audit every algorithm), the undercut is about the file he cannot convert, and the last two words carry the laugh. The detail is specific and unexpected — nobody converts a PDF by hand — rather than a worn tech-illiteracy cliché.

## Choosing the line

Three candidates were actually considered; the winner won on the turn, the aim on the rules lawmakers write, and the freshest detail.

1. **"The senator drafting the law to audit every algorithm on Earth just asked his intern to print the internet so he can convert it to PDF by hand."** — 143 chars. **Winner.** The grandest setup (a law to audit every algorithm on Earth) undercut by the smallest possible incompetence (converting to PDF by hand), with the punch on the last two words.
2. **"Congress just voted to rewrite the rules of artificial intelligence, and the bill's author is still on hold with IT because his .docx won't become a PDF."** — 153 chars. A clean turn and a specific .docx detail, but "on hold with IT" is a familiar office joke and the punch fades rather than lands.
3. **"They wrote a 400-page law on how machines must think, then called a hearing to ask why the PDF button keeps eating their homework."** — 130 chars. The 400-page law is a good setup, but "eating their homework" leans on the dog-ate-my-homework cliché, which the judge punishes.

The first draft of the winner was flatter — "The senator who wants to audit every algorithm on Earth just asked his intern to print the internet so he could convert it to PDF by hand." (138 chars) — and the revision changed "who wants to audit" to "drafting the law to audit" (the joke is now about the rules he writes, not just a wish) and "could" to "can" (present tense, the absurdity happening right now). See the revision note in `main.py`.

Referral code: 0txwmf1m

## License

MIT — see [LICENSE](LICENSE).
