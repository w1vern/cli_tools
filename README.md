# CLI Tools

A collection of handy CLI tools for everyday development tasks. Install and use them directly from your terminal.

## 📦 Installation

```bash
pip install git+https://github.com/w1vern/cli_tools
```

## 🛠 Available Tools

### 1. `env_generator`

Generates a unified `.env` file by merging all `.env.example` files in the specified directory and its subdirectories.

#### Usage:

```bash
env_generator --root path_to_root_dir --output path_to_result_file/.env
```

- `--root` *(optional)*: Path to the root directory to search for `.env.example` files. Defaults to the current directory.
- `--output` *(optional)*: Path to the resulting `.env` file. Defaults to `./.env`.

---

### 2. `one_file_generator`

Combines all project files (excluding those ignored by `.gitignore`) into a single text file, with section headers indicating the source of each file.

#### Usage:

```bash
one_file_generator --root path_to_root_dir --output path_to_result_file/.txt
```

- `--root` *(optional)*: Path to the root directory of the project. Defaults to the current directory.
- `--output` *(optional)*: Path to the output file. Defaults to `./project_dump.txt`.

---