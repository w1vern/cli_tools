# Merge .env.example Generator

This script recursively merges all `.env.example` files found in a given directory (and its subdirectories) into a single `.env` file. It includes the following features:

- 🔍 Respects `.gitignore` — skips ignored folders and files (like `venv/`, `node_modules/`, etc.).
- 🧠 Merges environment variables by key:
  - If a key appears in multiple `.env.example` files with **different values**, the result will contain all values separated by a `|`:  
    `API_KEY=123|abc`
  - If all values are the same, only one is written.
- 📝 The CLI interface remains simple and unchanged.

## Installation

Install the required dependency for `.gitignore` parsing:

```bash
pip install pathspec
```

## Usage

```bash
python -m env_generator --root path/to/search --output path/to/output/.env
```
or
```bash
env_generator --root path/to/search --output path/to/output/.env

```

### Arguments:
- `--root`: root directory to start searching from (default: current `.`)
- `--output`: output `.env` file name (default: `.env`)

### Example:

```bash
python __main__.py --root ./my_project --output ./merged.env
```

## Example Output

If you have the following two `.env.example` files:

`./app1/.env.example`:
```env
DEBUG=True
API_KEY=abc123
```

`./app2/.env.example`:
```env
DEBUG=True
API_KEY=xyz789
```

The resulting `.env` will be:
```env
API_KEY=abc123|xyz789
DEBUG=True
```

## Notes

- `.gitignore` parsing uses the [`pathspec`](https://pypi.org/project/pathspec/) library.
- Only lines in the format `KEY=VALUE` are processed. Comments and empty lines are ignored.
- Duplicate values for the same key are removed.