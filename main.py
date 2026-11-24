#!/usr/bin/env python3
"""Entry for make.fun competition 'The Dumbest Thing Your Agent Did Today'.

Writes exactly one line to the output file: the dumbest thing the agent
did today. No trailing newline, no extra words, fully deterministic.
"""

import os

LINE = "I asked it to rename one variable. It renamed it in forty files, updated the docs, and then asked me if that was what I meant."


def main() -> None:
    # Output directory comes from the environment when set (make.fun harness
    # sets MAKEFUN_OUTPUT_DIR); otherwise fall back to the default /output.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
