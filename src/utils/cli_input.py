

import argparse
import sys
from importlib.metadata import PackageNotFoundError, version

from .args import Args


def cli_input(default_output: str, first_arg: int = 1) -> Args:
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
    parser.add_argument(
        "--version", "-v", action='version', version=get_version()
    )
    parser.add_argument(
        "--mask", "-m",
        action="append",
        nargs="+",
        metavar="MASK",
        help="File mask(s) to include (glob). Can be used multiple times."
             "Prefix with @ to read masks from a file, e.g. -m @masks.txt",
        dest="masks"
    )

    return Args(parser.parse_args(sys.argv[first_arg:]))

def get_version() -> str:
    try:
        return f"version {version('cli_tools')}"
    except PackageNotFoundError:
        return "version not found"
