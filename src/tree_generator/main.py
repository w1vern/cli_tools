
import os
from pathlib import Path
from typing import TextIO

from utils import Args, cli_input, get_repo_files


class TreeNode:
    def __init__(self, name: str):
        self.name = name
        self.children = {}

    def add_path(self, parts: list[str]):
        if not parts:
            return
        head, *rest = parts
        if head not in self.children:
            self.children[head] = TreeNode(head)
        self.children[head].add_path(rest)

    def _write(self, file: TextIO, prefix: str = "", is_last: bool = True):
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{self.name}", file=file)
        prefix_child = prefix + ("    " if is_last else "│   ")
        child_count = len(self.children)
        for i, child in enumerate(sorted(self.children.values(), key=lambda c: (0 if c.children else 1, c.name.lower()))):
            child._write(file, prefix_child, i == child_count - 1)

    def write_tree(self, file: TextIO):
        print(self.name, file=file)
        child_count = len(self.children)
        for i, child in enumerate(sorted(self.children.values(), key=lambda c: (0 if c.children else 1, c.name.lower()))):
            child._write(file, "", i == child_count - 1)


def tree_generator(files: list[Path], args: Args) -> None:
    root = TreeNode(".")
    for path in files:
        parts = str(path).split(os.sep)
        root.add_path(parts)

    with open(args.output_file, "w", encoding="utf-8") as f:
        root.write_tree(f)


def main() -> None:
    args = cli_input("result.tree")
    files = get_repo_files(args)
    tree_generator(files, args)
    print(f"[✓] Successfully generated '{args.output_file}'")

