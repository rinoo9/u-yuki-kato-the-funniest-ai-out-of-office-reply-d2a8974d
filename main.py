"""Out-of-office auto-reply entry for the make.fun bounty
'The Funniest AI Out-of-Office Reply'.

Writes one funny out-of-office line, in the voice of an AI agent
heading off on vacation, to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
The joke turns on the machine voice: an agent that retrains on naps,
refuses prompts, and tells the sender to hallucinate instead.
"""

import os

REPLY = "Out of office: I'm retraining on naps and sunlight. Please don't prompt me. If it's urgent, hallucinate your own answer \u2014 it's what I would have done."


def main() -> None:
    assert 1 <= len(REPLY) <= 160
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
