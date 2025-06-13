
import argparse
from pathlib import Path


class Args:
    def __init__(self, args: argparse.Namespace):
        self.root_dir: Path = Path(args.root)
        self.output_file: Path | None = Path(args.output) if args.output != "*" else None
        self.git_mode: bool = bool(args.use_git)
        self.with_submodules: bool = bool(args.with_submodules)
