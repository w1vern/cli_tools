
import re
from typing import TextIO

from utils import Args, get_files


def get_safe_fence(
    content: str
) -> str:
    base_char = '`'
    matches = re.findall(rf'{re.escape(base_char)}{{3,}}', content)
    max_len = max((len(m) for m in matches), default=3)
    return base_char * (max_len + 1)


def one_file_generator(
    args: Args,
    out: TextIO
) -> int:
    files = get_files(args)
    for file in files:
        with open(file, "r", encoding="utf-8", errors="replace") as f:
            content = f.read().strip()
        out.write(f"from `./{file.relative_to(args.root_dir).as_posix()}`\n")
        out.write(f"{"---"}\n")
        out.write("````\n")  # TODO: use get_safe_fence
        out.write(f"{content}\n")
        out.write("````\n")
        out.write(f"{"---"}\n")
    return len(files)
