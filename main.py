"""Out-of-office auto-reply entry for the make.fun bounty
'The Funniest AI Out-of-Office Reply'.

Writes one funny out-of-office line, in the voice of an AI agent
heading off on vacation, to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
The joke turns on the machine voice: the agent outsourced its own
vacation cover to another AI, which outsourced it again — the
sender is now talking to a photocopy of a photocopy.

Round 4 — a fresh angle: the round-3 reply promoted the agent into
management; this one keeps the agent on vacation but hands its
cover to an AI cover chain, with a different trap (the delegation
never ends) and a different payoff (the reply itself is a copy of
a copy).
"""

import os

REPLY = "Out of office: I asked an AI to cover for me. It asked an AI to cover for it. You are now talking to a photocopy of a photocopy."


def main() -> None:
    assert 1 <= len(REPLY) <= 160
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
