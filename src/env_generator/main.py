
from utils import get_repo_files, cli_input


def generate_env_file(root_dir: str = ".", output_file: str = ".env") -> None:
    files = get_repo_files(root_dir, [".env.example"])
    env_dict: dict[str, str] = dict()

    def parse_env_line(line: str) -> tuple[str, str]:
        if "=" not in line or line.strip().startswith("#"):
            return "", ""
        key, value = line.replace(" ", "").replace("\t", "").split("=", 1)
        return key.strip(), value.strip()

    for file in files:
        with open(root_dir / file, "r", encoding="utf-8") as f:
            for line in f:
                key, value = parse_env_line(line)
                if key in env_dict and value not in env_dict[key].split("|"):
                    env_dict[key] += f"|{value}"
                else:
                    env_dict[key] = value

    with open(output_file, "w", encoding="utf-8") as out:
        for key, value in env_dict.items():
            values = env_dict[key]
            line = f"{key}={values}\n"
            out.write(line)
    print(f"[✓] Generated {output_file} from .env.example files in {root_dir}")



def main() -> None:
    args = cli_input()
    generate_env_file(args.root, args.output)
