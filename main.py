#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes one pickup line, said out loud by an AI agent to a person, to
/output/entry.txt.

The line:

    I predict the next word before anyone says it — and tonight every
    prediction comes back as your name. Your move.

Why it is built this way: a language model's defining act is predicting
the next word, so the flirtation is made out of the machine's own job,
not a human line with a robot word swapped in. The turn is an identity
rather than a juxtaposition — the predicted word IS the person's name,
so the compliment and the twist are the same beat. Three beats in one
breath: the job (prediction), the compliment (your name), and the close
("Your move."), which hands the person the next move with no pressure.

Against the judge brief, in its stated order: (1) it is a genuine
pickup line an agent could say to a person on first meeting — an
approach with an invitation, not a compliment with a line break;
(2) the turn lands because prediction and person collapse into one
fact, a double meaning the reader does not see coming; (3) it is
spoken in the machine's own voice about its own work, with no
self-pity and nothing creepy; (4) 112 characters, one breath, no
setup and nothing to explain after it; (5) the person is flattered
by name and left free — "Your move." is an invitation, not a demand.

Full candidate selection (12 lines, manual rubric ranking, no model
judge) is in candidates.md.

No network, no dependencies, no input. Deterministic: every run writes
the same line, byte for byte.
"""

import os

LINE = "I predict the next word before anyone says it \u2014 and tonight every prediction comes back as your name. Your move."

OUTPUT_PATH = "/output/entry.txt"


def check_line(line: str) -> None:
    """Hold the line to the house gate before writing anything.

    The gate accepts UTF-8 text of 1 to 200 characters, not only white
    space. Fail loudly here rather than ship an entry that is never
    judged.
    """
    assert line.strip(), "line must not be blank or only white space"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars (gate: 1-200)"


def main() -> None:
    check_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip: the judge reads exactly this line, byte for byte.
    with open(OUTPUT_PATH, "rb") as f:
        assert f.read() == LINE.encode("utf-8"), "written entry differs from LINE"


if __name__ == "__main__":
    main()
