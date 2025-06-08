# CLI Tools

A collection of handy CLI tools for everyday development tasks. Install and use them directly from your terminal.

## 📦 Installation

```bash
pip install git+https://github.com/w1vern/cli_tools
```

## 🛠 Available Tools

### 1. `env-generator`

Generates a unified `.env` file by merging all `.env.example` files in the specified directory and its subdirectories.

#### Usage:

```bash
env-generator --root path_to_root_dir --output path_to_result_file/.env
```

---

### 2. `one-file-generator`

Combines all project files (excluding those ignored by `.gitignore`) into a single text file, with section headers indicating the source of each file.

#### Usage:

```bash
one-file-generator --root path_to_root_dir --output path_to_result_file/.md
```

---

### 3. `tree-generator`

Print a hierarchical tree view of the project files and directories into single file (`result.tree` by default), starting from the specified root.

#### Usage:

```bash
tree-generator --root path_to_root_dir --output path_to_result_file/.tree
```

## ⚙️ Common Flags

The following flags are shared across all CLI utilities in this collection:

| Flag                | Shortcut | Description                                  | Default                                                             |
|---------------------|----------|----------------------------------------------|---------------------------------------------------------------------|
| `--root`            | `-r`     | Root directory to start searching or working | Current directory (`.`)                                             |
| `--output`          | `-o`     | Output file path                             | Utility-specific default (e.g., `.env`, `result.tree`, `result.md`) |
| `--off-git-mode`    | `-og`    | Disable git mode                             | Enabled by default                                                  |
| `--with-submodules` | `-ws`    | Include git submodules from processing       | Exclude submodules by default                                       |

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
