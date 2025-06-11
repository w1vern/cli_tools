
from typing import TextIO

from utils import Args, get_files


def env_generator(args: Args, out: TextIO) -> int:
    files = get_files(args, [".env.example"])
    env_dict: dict[str, str] = dict()

    def parse_env_line(line: str) -> tuple[str, str] | None:
        if "=" not in line or line.strip().startswith("#"):
            return None
        key, value = line.replace(" ", "").replace("\t", "").split("=", 1)
        return key.strip(), value.strip()

    for file in files:
        with open(file, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                parsed = parse_env_line(line)
                if not parsed:
                    continue
                key, value = parsed
                if key in env_dict and value not in env_dict[key].split("|"):
                    env_dict[key] += f"|{value}"
                else:
                    env_dict[key] = value
    for key, value in env_dict.items():
        values = env_dict[key]
        line = f"{key}={values}\n"
        out.write(line)
    return len(files)
