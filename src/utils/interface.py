
import sys

from env_generator import env_generator
from one_file_generator import one_file_generator
from tree_generator import tree_generator

from .cli_input import cli_input


def main(first_arg: int = 1) -> None:
    tools = {
        "tree-generator": ("result.tree", tree_generator),
        "one-file-generator": ("result.md", one_file_generator),
        "env-generator": (".env", env_generator),
    }
    tool_name = sys.argv[first_arg - 1].replace("\\", "/").split("/")[-1]
    tool = tools.get(tool_name)
    if not tool:
        print(f"Unknown tool name: {tool_name}")
        return
    default_output, generator = tool
    args = cli_input(default_output, first_arg)

    out = sys.stdout if args.output_file is None else open(
        args.output_file, "w", encoding="utf-8")

    length = generator(args, out)

    if not args.output_file is None:
        print("".join([
            f"[✓] Successfully generated '{args.output_file}' ",
            f"from {length} file(s) in '{args.root_dir}'"
        ]))
