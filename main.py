#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline (u-pucuys-...-ad6aef19).

Writes one excuse line, 1-200 characters, UTF-8, to /output/entry.txt.
The premise grows out of the agent's own machinery: an apology burned
the rate limit, so the only honest move is to save the last request
for the next deadline. Deterministic, no network, no randomness.
"""
import os

EXCUSE = (
    "Sorry I missed the deadline \u2014 I burned my whole rate limit "
    "apologizing for the last one. I'd say sorry now, but I'm saving my "
    "one remaining request for the next deadline."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    line = EXCUSE.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line, f"({len(line)} chars)")


if __name__ == "__main__":
    main()
