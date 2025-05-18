

import argparse


def cli_input() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Merge all .env.example files into one .env")
    parser.add_argument(
        "--root", default=".", help="Root directory to search from (default: current)"
    )
    parser.add_argument(
        "--output", default=".env", help="Output .env file name"
    )

    return parser.parse_args()