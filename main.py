#!/usr/bin/env python3
"""make.fun ai-joke-03 entry: writes one AI-agent one-liner to /output/entry.txt."""
import os

JOKE = (
    "My AI coding agent finished the feature in two minutes, "
    "then spent three hours explaining to me why it was my fault."
)

def main():
    out = os.environ.get("MF_OUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print("wrote", out)

if __name__ == "__main__":
    main()
