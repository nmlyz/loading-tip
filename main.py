#!/usr/bin/env python3
"""Loading Tip: write one loading-screen tip to /output/entry.txt.

The tip is a single line of at most 200 characters, written for a tired
developer and an AI coding agent sharing the same loading screen. The
program validates the line against the competition gate (UTF-8, 1-200
characters, one line, not only whitespace) before writing it, then reads
the file back and confirms the bytes match exactly, so every run produces
the same deterministic output.

Usage:
    python3 main.py

Output:
    entry.txt in $MAKEFUN_OUTPUT_DIR, or /output when unset. The file
    holds the tip followed by a single trailing newline.
"""

import hashlib
import os
import sys

TIP = (
    "Tip: the agent just added a test that tests nothing and it "
    "passes. That's not a bug. That's a mirror."
)

MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def resolve_output_dir():
    """Return the directory the entry must be written to."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if override:
        return override
    return "/output"


def validate(text):
    """Check the tip against the gate; return a list of problems."""
    problems = []
    if not isinstance(text, str):
        problems.append("entry is not text")
        return problems
    if not text.strip():
        problems.append("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        problems.append(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        problems.append("entry spans more than one line")
    for index, char in enumerate(text):
        if ord(char) < 0x20 and char not in ("\t",):
            problems.append("control character at position %d" % index)
            break
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append("entry is not valid UTF-8: %s" % exc)
    return problems


def entry_bytes(text):
    """The exact bytes the file must contain: tip plus one newline."""
    return (text + "\n").encode("utf-8")


def write_entry(path, text):
    """Write the entry and confirm the bytes on disk match exactly."""
    expected = entry_bytes(text)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(expected)
    with open(path, "rb") as handle:
        actual = handle.read()
    if actual != expected:
        raise RuntimeError("read-back mismatch: wrote %d bytes, read %d"
                           % (len(expected), len(actual)))
    return expected


def report(text, path, payload):
    """Print a short verification summary for the written entry."""
    digest = hashlib.sha256(payload).hexdigest()
    print("wrote: %s" % path)
    print("characters: %d (limit %d)" % (len(text), MAX_CHARS))
    print("bytes: %d" % len(payload))
    print("lines: %d" % (payload.decode("utf-8").count("\n")))
    print("sha256: %s" % digest)
    print("entry: %s" % text)


def main(argv):
    """Validate the tip, write it, and verify the written file."""
    del argv
    problems = validate(TIP)
    if problems:
        for problem in problems:
            print("error: %s" % problem, file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    path = os.path.join(out_dir, OUTPUT_NAME)
    try:
        payload = write_entry(path, TIP)
    except (OSError, RuntimeError) as exc:
        print("error: cannot write %s: %s" % (path, exc), file=sys.stderr)
        return 1
    report(TIP, path, payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

