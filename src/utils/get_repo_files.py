

from pathlib import Path
from time import sleep
from pathspec import PathSpec


def load_gitignore_lines(dir_path: str) -> list[str]:
    path = Path(dir_path) / ".gitignore"
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return [_.replace("\n", "").replace(" ", "") for _ in f.readlines()]


def parse_dir(dir_path: str,
              file_masks: list[str],
              repo_files: list[Path],
              ignore: list[str]
              ) -> None:
    folder = Path(dir_path)
    if not folder.is_dir():
        raise ValueError(f"{dir_path} is not a directory (internal error)")
    git_folder = folder / ".git"
    """ if git_folder.is_dir():
        local_ignore = []
    else: """
    local_ignore = ignore.copy()
    local_ignore += load_gitignore_lines(dir_path)
    pathspec_ignore = PathSpec.from_lines("gitwildmatch", local_ignore)
    for item in folder.iterdir():
        if item.is_dir():
            if pathspec_ignore.match_file(f"{item.relative_to(folder)}/"):
                continue
            if item.name == '.git':
                continue
            parse_dir(str(item), file_masks, repo_files, ignore)
        elif item.is_file():
            if pathspec_ignore.match_file(item):
                continue
            use_file = False
            for mask in file_masks:
                if item.match(mask):
                    use_file = True
                    break
            if use_file:
                repo_files.append(item)
        else:
            raise ValueError(
                f"{item} is not a file or directory (internal error)")


def get_repo_files(root_dir: str,
                   file_masks: list[str] = ["*"]
                   ) -> list[Path]:
    repo_files: list[Path] = []
    parse_dir(root_dir,
              file_masks,
              repo_files,
              ignore=[])
    return repo_files
