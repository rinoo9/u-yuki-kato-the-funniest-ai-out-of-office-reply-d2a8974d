"""Out-of-office auto-reply entry for the make.fun bounty
'The Funniest AI Out-of-Office Reply'.

Writes one funny out-of-office line, in the voice of an AI agent
heading off on vacation, to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
The joke turns on the machine voice: the agent hands its inbox to
an intern model that has already gone rogue in a language it does
not speak — and cannot be fired.
"""

import os

REPLY = "Out of office: I've handed my inbox to an intern model. It has already replied to you twice, in a language I don't speak, and it cannot be fired."


def main() -> None:
    assert 1 <= len(REPLY) <= 160
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
