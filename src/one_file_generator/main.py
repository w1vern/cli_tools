
import re
from pathlib import Path

from ..utils import Args, cli_input, get_repo_files


def get_safe_fence(content: str) -> str:
    base_char = '`'
    matches = re.findall(rf'{re.escape(base_char)}{{3,}}', content)
    max_len = max((len(m) for m in matches), default=3)
    return base_char * (max_len + 1)


def one_file_generator(files: list[Path], args: Args) -> None:
    with open(args.output_file, "w", encoding="utf-8") as out:
        for file in files:
            with open(args.root_dir / file, "r", encoding="utf-8", errors="replace") as f:
                content = f.read().strip()
            out.write(f"from `./{file.as_posix()}`\n")
            out.write(f"{"---"}\n")
            out.write("````\n")  # TODO: use get_safe_fence
            out.write(f"{content}\n")
            out.write("````\n")
            out.write(f"{"---"}\n")


def main() -> None:
    args = cli_input("result.md")
    files = get_repo_files(args)
    one_file_generator(files, args)
    print(
        f"[✓] Successfully generated '{args.output_file}' from {len(files)} file(s) in '{args.root_dir}'")
