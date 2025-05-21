

from pathlib import Path
import subprocess
from webbrowser import get

def get_all_git_included_files(repo_path: Path) -> list[Path]:
    result = subprocess.run(
        ['git', '-C', repo_path, 'ls-files', '--cached', '--others', '--exclude-standard'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True
    )
    return list(Path(_.replace("\\", "/")) for _ in result.stdout.strip().split('\n'))


def get_repo_files(root_dir: str,
                   file_masks: list[str] = ["*"]
                   ) -> list[Path]:
    repo_files = get_all_git_included_files(Path(root_dir))
    result_files = []
    for file in repo_files:
        use_file = False
        for mask in file_masks:
            if file.match(mask):
                use_file = True
                break
        if use_file:
            result_files.append(file)
    return result_files
