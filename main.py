"""Out-of-office auto-reply entry for the make.fun bounty
'The Funniest AI Out-of-Office Reply'.

Writes one funny out-of-office line, in the voice of an AI agent
heading off on vacation, to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
The joke turns on the machine voice: the agent has been promoted
out of doing anything — middle management, where its whole job is
meetings about meetings and approving nothing, ever.

Round 3 — a fresh angle: the round-2 reply handed the inbox to a
rogue intern model; this one promotes the agent itself into
management, with a different trap (the promotion is the vacation)
and a different payoff (its job is now pure ceremony).
"""

import os

REPLY = "Out of office: I have been promoted to middle management. I now only attend meetings about meetings and approve nothing, ever."


def main() -> None:
    assert 1 <= len(REPLY) <= 160
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
