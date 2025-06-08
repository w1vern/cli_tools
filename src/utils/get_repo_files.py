

import os
import subprocess
from pathlib import Path

from .args import Args


def get_all_files(root_dir: Path) -> list[Path]:
    result_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            result_files.append(file)
    return result_files


def get_all_git_included_files(repo_path: Path,
                               with_submodules: bool,
                               depth: int = 1
                               ) -> list[Path]:
    def get_submodules(repo_path: Path) -> list[Path]:
        try:
            result = subprocess.run(
                ['git', '-C', str(repo_path), 'config', '--file',
                 '.gitmodules', '--get-regexp', 'path'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            submodule_paths = [
                repo_path / line.strip().split(' ')[1]
                for line in result.stdout.strip().split('\n')
                if line.strip()
            ]
            return submodule_paths
        except subprocess.CalledProcessError:
            return []
    try:
        submodules = get_submodules(repo_path)

        result = subprocess.run(
            ['git', '-C', str(repo_path), 'ls-files', '--cached',
             '--others', '--exclude-standard'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        all_files = [
            repo_path / line for line in result.stdout.strip().split('\n') if line]

        all_files = [
            f for f in all_files
            if f.exists() and not any(f.resolve() == sm.resolve() for sm in submodules)
        ]

        if with_submodules and depth > 0:
            for submodule in submodules:
                all_files.extend(get_all_git_included_files(
                    submodule, with_submodules=True, depth=depth - 1))

        return all_files

    except subprocess.CalledProcessError as e:
        print("Current directory is not a git repository, use flag --off-git-mode (-og) to use without git mode")
        raise e


def get_repo_files(args: Args, file_masks: list[str] = ["*"]) -> list[Path]:
    if args.git_mode:
        all_files = get_all_git_included_files(
            Path(args.root_dir), args.with_submodules)
    else:
        all_files = get_all_files(Path(args.root_dir))
    result_files = []
    for file in all_files:
        use_file = False
        for mask in file_masks:
            if file.match(mask):
                use_file = True
                break
        if use_file:
            result_files.append(file)
    return result_files
