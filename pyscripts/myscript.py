import argparse
import logging
import sys
from datetime import datetime

#!/usr/bin/env python3
"""
Basic Python script template.

Usage:
    python myscript.py --name Alice --count 3
"""



def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Simple greeting script")
    p.add_argument("--name", "-n", default="World", help="Name to greet")
    p.add_argument("--count", "-c", type=int, default=1, help="How many times to greet")
    return p.parse_args(argv)


def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")


def greet(name: str, count: int):
    for i in range(count):
        logging.info("Hello, %s! (%d/%d) - %s", name, i + 1, count, datetime.now().isoformat())


def main(argv=None) -> int:
    setup_logging()
    args = parse_args(argv)
    greet(args.name, args.count)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())