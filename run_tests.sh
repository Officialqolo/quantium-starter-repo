#!/bin/bash

# Exit immediately if a command exits with a non‑zero status
set -e

# -------------------------------
# 1. Activate the virtual environment
# -------------------------------
# Adjust path if your venv folder is named differently (e.g., venv, .venv, env)

source venv/bin/activate

# -------------------------------
# 2. Run the test suite
# -------------------------------
pytest -v

# -------------------------------
# 3. If pytest fails, exit code will be 1 automatically because of `set -e`
# If pytest passes, script reaches here → return exit code 0
# -------------------------------
echo "All tests passed successfully!"
exit 0
