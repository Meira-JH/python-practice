# Python Practice

Repository of Python practice exercises for refreshing fundamentals.

## What This Environment Includes

This repo is set up for a small local Python practice workflow:

- Python 3.12 or newer for running scripts and exercises.
- A local virtual environment in `.venv/` so packages stay isolated from your system Python.
- `pytest` for writing and running practice checks.
- `ruff` for linting and formatting Python code.
- `ipython` for a friendlier interactive Python shell.

The `.venv/` folder is intentionally ignored by Git, so each machine can create its own local environment.

## Setup

From the repo root, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Upgrade `pip` and install the practice tools:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

### You only need to create the environment once. For future sessions, activate it again with:

```bash
source .venv/bin/activate
```

## Verify Everything Works

Run these commands after activating the environment:

```bash
python --version
pytest
ruff check .
```

You should see Python 3.12 or newer, a passing test run, and no lint errors.

## Practicing Fundamentals

Use `exercises/` for practice code and `tests/` for small checks.

Example workflow:

```bash
mkdir -p exercises tests
touch exercises/basics.py tests/test_basics.py
pytest
```

For quick experiments, open an interactive shell:

```bash
ipython
```

For formatting and linting:

```bash
ruff format .
ruff check .
```

When you are done working, you can leave the virtual environment with:

```bash
deactivate
```

## Troubleshooting

If `python3` is not found, install Python 3.12 or newer first. On macOS, good options are:

- `mise install python@3.12`
- `brew install python`

If package installation fails, make sure the virtual environment is activated and try:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```


## Tests

```bash
./.venv/bin/pytest tests/[path]/[file-name].py
```