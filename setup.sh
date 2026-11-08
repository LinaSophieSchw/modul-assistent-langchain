#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
PYTHON_BIN="${PYTHON_BIN:-python3.13}"
"$PYTHON_BIN" -m venv .venv
.venv/bin/python -c "import sys; assert sys.version_info[:2] in ((3,12),(3,13)), 'Python 3.12 oder 3.13 erforderlich'"
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip install -e .
.venv/bin/python -m jupyterlab notebooks
