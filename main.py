#!/usr/bin/env python3
"""Museum of the Year 3000 — writes the museum label for one ordinary object."""
import os
import sys

LABEL = "Group chat, c. 2025. A ritual scroll where humans gathered daily to speak at once and listen to no one, then called it friendship."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    text = LABEL.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")

if __name__ == "__main__":
    main()
