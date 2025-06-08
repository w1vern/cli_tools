

import argparse

from .args import Args


def cli_input(default_output: str) -> Args:
    parser = argparse.ArgumentParser(
        description="Merge all .env.example files into one .env")
    parser.add_argument(
        "--root", "-r", default=".", help="Root directory (default: current)", dest="root"
    )
    parser.add_argument(
        "--output", "-o", default=f"{default_output}", help="Output file name", dest="output"
    )
    parser.add_argument(
        "--off-git-mode", "-og", action="store_false", help="Disable git mode", dest="use_git"
    )
    parser.add_argument(
        "--with-submodules", "-ws", action="store_true", help="Do not include submodules", dest="with_submodules"
    )

    return Args(parser.parse_args())
