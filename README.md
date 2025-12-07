# Advent of Code 2025

Repository to solve Advent of Code 2025 problems in Python. Each day gets its own module under `days/` and the `run_all.py` runner executes available days and collects output.

Structure

- `days/` — day solutions (e.g., `day01.py`, `day02.py`)
- `run_all.py` — simple runner to execute day scripts
- `requirements.txt` — third-party dependencies (if any)

Getting started

1. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run the runner:

```powershell
python run_all.py
```

Push to GitHub

- Initialize git and push: `git init; git add .; git commit -m "Initial scaffold"; git branch -M main; git remote add origin <repo-url>; git push -u origin main` 
- Or use `gh repo create` to make and push the repo in one command.
