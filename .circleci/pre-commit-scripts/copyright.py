"""Keeps the Year in Coypright files up to date."""

import argparse
import re
from datetime import datetime
from typing import Sequence, Optional


def main(argv: Optional[Sequence[str]] = None):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check.")
    args = parser.parse_args(argv)

    filenames = args.filenames
    if not filenames:
        from pathlib import Path

        repo_root = Path(__file__).parent.parent.parent.resolve()
        assert (repo_root / "LICENSE").exists(), f"Not Repo Root. {repo_root}"
        filenames = [f for f in repo_root.rglob("Dockerfile*")]

    for filename in filenames:
        with open(filename, "r") as file:
            s = file.read()
        ns = re.sub(
            r"# Copyright (\d{4}) Astronomer Inc.",
            f"# Copyright {datetime.now().year} Astronomer Inc.",
            s,
            flags=re.MULTILINE,
        )
        with open(filename, "w") as file:
            file.write(ns)


if __name__ == "__main__":
    raise SystemExit(main())
