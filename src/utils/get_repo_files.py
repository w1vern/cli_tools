

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


def get_all_git_included_files(repo_path: Path, with_submodules: bool) -> list[Path]:
    try:
        result = subprocess.run(
            ['git', '-C', repo_path, 'ls-files', '--cached',
                '--others', '--exclude-standard'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return list(Path(_) for _ in result.stdout.strip().split('\n'))
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
