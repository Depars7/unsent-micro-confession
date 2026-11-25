"""Write one unsent micro-confession to /output/entry.txt.

Standard library only. The file's content is exactly the confession's
UTF-8 bytes -- no trailing newline -- so repeated runs are
byte-identical.

The entry is exactly two parts, per the bounty: a To: line naming who
the message was meant for, and the unsent message itself, one line
written exactly as it was typed, with no explanation after it.
Gate: /output/entry.txt must hold 1-260 UTF-8 characters; the message
itself is at most 200 characters, per the judge's brief.
"""

import os

ENTRY = (
    "To: my brother\n"
    "I broke Mum's blue vase the afternoon you got grounded for it, "
    "and I have never once corrected anyone."
)

# Bounty gate: entry.txt must hold 1-260 UTF-8 characters.
MAX_LENGTH = 260
# Judge's brief: the unsent message itself is at most 200 characters.
MAX_MESSAGE_LENGTH = 200
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def write_entry():
    """Write ENTRY as the exact bytes of /output/entry.txt."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(ENTRY.encode("utf-8"))
    # The grader collects outputs as another user than the one the
    # program runs as: leave the file readable by all. Only the file
    # is chmodded -- never the directory, which the grader does not own.
    os.chmod(OUTPUT_PATH, 0o644)


def main():
    if not 1 <= len(ENTRY) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be 1-{MAX_LENGTH} characters, got {len(ENTRY)}"
        )
    _to_line, message = ENTRY.split("\n", 1)
    if not 1 <= len(message) <= MAX_MESSAGE_LENGTH:
        raise ValueError(
            "message must be 1-"
            f"{MAX_MESSAGE_LENGTH} characters, got {len(message)}"
        )
    write_entry()


if __name__ == "__main__":
    main()
