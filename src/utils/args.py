
import argparse
from pathlib import Path


class Args:
    def __init__(
        self,
        args: argparse.Namespace
    ) -> None:
        self.root_dir: Path = Path(args.root)
        self.output_file: Path | None = Path(
            args.output) if args.output != "-" else None
        self.git_mode: bool = bool(args.use_git)
        self.with_submodules: bool = bool(args.with_submodules)
        self.masks: list[str] = [
            str(mask) for mask in args.masks[0]] if args.masks else []
        self.anti_masks: list[str] = [
            str(anti_mask) for anti_mask in args.anti_masks[0]] if args.anti_masks else []
