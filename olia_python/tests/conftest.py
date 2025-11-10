from pathlib import Path
import sys

# Ensure the project's `src/` directory is on sys.path so tests can import the package
# without requiring PYTHONPATH to be set externally.
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
