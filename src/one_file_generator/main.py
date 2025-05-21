
from utils import cli_input, get_repo_files

def one_file_generator(root_dir: str = ".", output_file: str = "result") -> None:
    files = get_repo_files(root_dir)
    with open(output_file, "w", encoding="utf-8") as out:
        for file in files:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read().strip()
            out.write(f"from ./{file.as_posix()}\n")
            out.write(f"{"-" * 100}\n")
            out.write(f"{content}\n")
            out.write(f"{"-" * 100}\n")

    print(f"[✓] Successfully generated '{output_file}' from {len(files)} file(s) in '{root_dir}'")




def main() -> None:
    args = cli_input()
    one_file_generator(args.root, args.output)