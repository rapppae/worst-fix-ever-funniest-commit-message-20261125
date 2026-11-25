"""Entry for Worst Fix Ever: Funniest Commit Message.

Slug: u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722
"""

import os

# Entry: 68 characters (limit: at most 100 characters).
ENTRY = "fix: stop the leak by deleting the bucket, the floor, and production"


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
