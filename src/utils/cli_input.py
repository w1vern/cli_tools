
import argparse
import sys
from importlib.metadata import PackageNotFoundError, version

from .args import Args


def cli_input(
    default_output: str,
    first_arg: int = 1
) -> Args:
    parser = argparse.ArgumentParser(
        description="Set of useful cli tools")
    parser.add_argument(
        "--root", "-r", default=".", help="Root directory (default: current)", dest="root"
    )
    parser.add_argument(
        "--output", "-o", default=f"{default_output}", help="Output file name", dest="output"
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
        help="File mask(s) to include (glob). Can be used multiple times.",
        dest="masks"
    )
    parser.add_argument(
        "--anti-mask", "-am",
        action="append",
        nargs="+",
        metavar="ANTI_MASK",
        help="File mask(s) to exclude (glob). Can be used multiple times.",
        dest="anti_masks"
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--git-mode", "-g", action="store_true", help="Enable git mode", dest="use_git"
    )
    group.add_argument(
        "--off-git-mode", "-og", action="store_false", help="Disable git mode", dest="use_git"
    )
    parser.set_defaults(use_git=None)

    return Args(parser.parse_args(sys.argv[first_arg:]))


def get_version() -> str:
    try:
        return f"version {version('cli_tools')}"
    except PackageNotFoundError:
        return "version not found"
