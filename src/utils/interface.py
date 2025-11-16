
import sys

from env_generator import env_generator
from one_file_generator import one_file_generator
from tree_generator import tree_generator

from .cli_input import cli_input


def main(
    first_arg: int = 1
) -> None:
    tools = {
        0: ("result.tree", tree_generator),
        1: ("result.md", one_file_generator),
        2: (".env", env_generator),
    }
    aliases = {
        "tg": 0,
        "tree-generator": 0,
        "ofg": 1,
        "one-file-generator": 1,
        "eg": 2,
        "env-generator": 2,
    }
    tool_name = sys.argv[first_arg - 1].replace("\\", "/").split("/")[-1]
    tool_id = aliases.get(tool_name)
    if tool_id is None:
        print(f"Unknown tool name: {tool_name}")
        return
    tool = tools[tool_id]
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
