
import argparse
from pathlib import Path


class Args:
    def __init__(self, args: argparse.Namespace):
        self.root_dir: Path = args.root
        self.output_file: Path = args.output
        self.git_mode: bool = args.use_git
        self.with_submodules: bool = args.with_submodules
