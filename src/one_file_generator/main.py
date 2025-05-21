
from utils import Args, cli_input, get_repo_files


def one_file_generator(args: Args) -> None:
    files = get_repo_files(args)
    with open(args.output_file, "w", encoding="utf-8") as out:
        for file in files:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read().strip()
            out.write(f"from ./{file.as_posix()}\n")
            out.write(f"{"-" * 100}\n")
            out.write(f"{content}\n")
            out.write(f"{"-" * 100}\n")

    print(f"[✓] Successfully generated '{args.output_file}' from {len(files)} file(s) in '{args.root_dir}'")




def main() -> None:
    args = cli_input("result.txt")
    one_file_generator(args)