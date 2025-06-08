
from pathlib import Path

from utils import Args, cli_input, get_repo_files


def generate_env_file(files: list[Path], args: Args) -> None:
    files = get_repo_files(args, [".env.example"])
    env_dict: dict[str, str] = dict()

    def parse_env_line(line: str) -> tuple[str, str]:
        if "=" not in line or line.strip().startswith("#"):
            return "", ""
        key, value = line.replace(" ", "").replace("\t", "").split("=", 1)
        return key.strip(), value.strip()

    for file in files:
        with open(args.root_dir / file, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                key, value = parse_env_line(line)
                if key in env_dict and value not in env_dict[key].split("|"):
                    env_dict[key] += f"|{value}"
                else:
                    env_dict[key] = value

    with open(args.output_file, "w", encoding="utf-8") as out:
        for key, value in env_dict.items():
            values = env_dict[key]
            line = f"{key}={values}\n"
            out.write(line)


def main() -> None:
    args = cli_input(".env")
    files = get_repo_files(args)
    generate_env_file(files, args)
    print(f"[✓] Generated {args.output_file} from .env.example files in {args.root_dir}")
