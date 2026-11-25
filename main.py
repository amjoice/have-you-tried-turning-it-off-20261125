"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line from a hopeless tech support agent to
/output/entry.txt. Standard library only; deterministic; no network.
"""

import os

LINE = "I'm escalating this to Tier 2, which is me, but with a different hat."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
