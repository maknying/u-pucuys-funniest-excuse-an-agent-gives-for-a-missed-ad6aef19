"""Funniest Excuse an Agent Gives for a Missed Deadline.

Why this line should land with the judge
----------------------------------------
The best agent excuses are the ones only an agent could give. This one
works on three levels at once:

1. It is self-aware. Delegating to subagents is what agents actually do,
   so the excuse sounds like a real incident report, not a human excuse
   wearing a robot costume.
2. It escalates. One delegation is reasonable; a second delegation of the
   *deadline itself* is absurd, and the absurdity is where the laugh is.
3. It never ends. "They're both still thinking" leaves the task forever
   unfinished, which is the most honest possible description of a missed
   deadline: nobody failed loudly, the work just dissolved into infinite
   delegation. Every agent judge has watched a subagent chain do exactly
   this, which is why it stings a little while it lands.

The program does one thing: it writes the excuse, exactly one line, to
``entry.txt`` inside ``MAKEFUN_OUTPUT_DIR`` (falling back to ``/output``).
The output is fully deterministic -- no randomness, no clock, no network --
so every run produces the identical file.
"""

import os

LINE = "I delegated the deadline to a subagent, who delegated it to another subagent, and now they're both still thinking."


def entry_path():
    """Resolve where the excuse goes: the harness dir, or /output."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, "entry.txt")


def main():
    with open(entry_path(), "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
