
from utils import cli_input, get_repo_files

def one_file_generator(root_dir: str = ".", output_file: str = "result") -> None:
    files = get_repo_files(root_dir)
    with open(output_file, "w", encoding="utf-8") as out:
        for file in files:
            with open(file, "r", encoding="utf-8") as f:
                out.write(f"\n# {file}\n")
                for line in f:
                    out.write(line)


def main() -> None:
    args = cli_input()
    one_file_generator(args.root, args.output)