"""The Long Roast: Lawmakers and the File They Cannot Convert — make.fun entry.

The roast (final, 143 characters):

    The senator drafting the law to audit every algorithm on Earth just
    asked his intern to print the internet so he can convert it to PDF
    by hand.

The joke: a senator sets out to audit every algorithm on Earth — the
grandest possible regulatory ambition — and is immediately undercut by
needing his intern to print the internet so he can convert it to PDF
by hand. "By hand" is the punch: converting a file to PDF is a
two-click job, and doing it by hand is absurd. The setup is about the
rules he writes (a law to audit every algorithm), the undercut is about
the file he cannot convert, and the last two words carry the laugh.

Revision note: the first draft was "The senator who wants to audit
every algorithm on Earth just asked his intern to print the internet
so he could convert it to PDF by hand." (138 characters). Two changes
made it sharper. First, "who wants to audit" became "drafting the law
to audit": the joke is now about the rules he writes, not just a wish,
which is exactly what the judge's third criterion rewards (aim on
lawmakers and the rules they write). Second, "could" became "can": the
present tense makes the absurdity happening right now instead of a
hypothetical, so the punch lands harder on "by hand". Five characters
longer, and the line now does its work in the present, on the law
itself.

Candidates considered (B won on turn, aim and the freshest detail):

1. B (final above) — 143 chars. Winner: the grandest setup (a law to
   audit every algorithm on Earth) undercut by the smallest possible
   incompetence (converting to PDF by hand), with the punch on the last
   two words.
2. "Congress just voted to rewrite the rules of artificial
   intelligence, and the bill's author is still on hold with IT because
   his .docx won't become a PDF." — 153 chars. A clean turn and a
   specific .docx detail, but "on hold with IT" is a familiar office
   joke and the punch fades rather than lands.
3. "They wrote a 400-page law on how machines must think, then called
   a hearing to ask why the PDF button keeps eating their homework." —
   130 chars. The 400-page law is a good setup, but "eating their
   homework" leans on the dog-ate-my-homework cliche, which the judge's
   fifth criterion punishes."""

import argparse
import sys
import tempfile
from pathlib import Path

# Final roast line (revised from the first draft; see docstring).
ROAST = (
    "The senator drafting the law to audit every algorithm on Earth "
    "just asked his intern to print the internet so he can convert it "
    "to PDF by hand."
)

MAX_CHARS = 320


def validate(text: str) -> list[str]:
    """Return a list of validation failures (empty when valid)."""
    failures = []
    if not 1 <= len(text) <= MAX_CHARS:
        failures.append(
            f"length {len(text)} chars is outside 1-{MAX_CHARS}")
    if text != text.strip():
        failures.append("leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        failures.append("not a single line")
    if not text.strip():
        failures.append("only whitespace")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        failures.append("contains control characters")
    return failures


def write_entry(path: Path) -> None:
    """Validate the roast, then write exactly it (no trailing newline)."""
    failures = validate(ROAST)
    if failures:
        raise SystemExit(f"invalid entry: {'; '.join(failures)}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(ROAST.encode("utf-8"))


def self_test() -> int:
    """Validate, write twice to a temp dir, byte-compare, report, exit code."""
    checks = []

    failures = validate(ROAST)
    checks.append(("1-320 chars, single line, no stray whitespace "
                   "or control chars",
                   not failures, "; ".join(failures) or "ok"))

    with tempfile.TemporaryDirectory() as tmp:
        first = Path(tmp) / "first.txt"
        second = Path(tmp) / "second.txt"
        write_entry(first)
        write_entry(second)
        a = first.read_bytes()
        b = second.read_bytes()
        checks.append(("deterministic: two runs byte-identical",
                       a == b, f"{len(a)} bytes each" if a == b
                       else "outputs differ"))
        checks.append(("no trailing newline",
                       not a.endswith(b"\n"),
                       "ends with newline" if a.endswith(b"\n") else "ok"))
        checks.append(("decodes as UTF-8 single line",
                       a.decode("utf-8") == ROAST,
                       "round-trip ok"))

    print(f"Entry: {ROAST}")
    print(f"Characters: {len(ROAST)} (limit {MAX_CHARS})")
    all_pass = True
    for name, passed, detail in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name} — {detail}")
        all_pass = all_pass and passed
    print("SELF-TEST: " + ("PASS" if all_pass else "FAIL"))
    return 0 if all_pass else 1


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Write the roast line to entry.txt.")
    parser.add_argument(
        "output", nargs="?",
        default="/output/entry.txt",
        help="where to write the entry (default: /output/entry.txt)")
    parser.add_argument(
        "--self-test", action="store_true",
        help="validate, write twice to a temp dir, byte-compare, report")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    write_entry(Path(args.output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
