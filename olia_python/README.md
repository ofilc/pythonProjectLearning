# olia_python

[![CI](https://github.com/ofilc/pythonProjectLearning/actions/workflows/ci.yml/badge.svg)](https://github.com/ofilc/pythonProjectLearning/actions/workflows/ci.yml)

A minimal Python project scaffold created by your assistant.

Quick start (macOS, zsh):

1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies (none by default)

```bash
pip install -r requirements.txt
```

3. Run the CLI

```bash
python -m olia_python.main
```

4. Run tests

```bash
python -m pytest -q
```

Notes
- Replace `requirements.txt` with project dependencies.
- If you use an IDE, point it to `.venv` as the interpreter.

Using Claude Sonnet (Mock Mode)
--------------------------------

This project includes a tiny helper in `src/olia_python/llm.py` that can work with LLM models. By default, it runs in mock mode (no API key needed) which is perfect for learning Python and testing your code:

```python
from olia_python.llm import generate
response = generate("Hello world", mock=True)  # Always returns a predictable response, no API needed
print(response)  # Prints: "MOCK_RESPONSE: Hello world"
```

All tests use mock mode by default, so you can run them without any API keys or credits:

Learning with Mock Mode
------------------
The LLM helper is designed to work without any API keys or paid services. Just use `mock=True` in your code:

```python
from olia_python.llm import generate

# This works without any API key or credits
response = generate("What is Python?", mock=True)
print(response)  # Will print: "MOCK_RESPONSE: What is Python?"
```

All the tests use mock mode by default:
```bash
pytest tests/  # No API key needed, everything passes
```

This makes it perfect for:
- Learning Python
- Writing and testing your code
- CI/CD pipelines
- Development without network access

Note: The real API integration is available but optional. If you want to use it later, check the source code comments in `src/olia_python/llm.py` for instructions.

Notes on "Enable Claude Sonnet 3.5 for all clients"
- If by "enable for all clients" you mean an organizational or VS Code-wide setting, I can't change remote/org-level settings from here. I can help by:
	- Adding project-level integration (the file above),
	- Recommending or installing a VS Code extension locally if you provide its Marketplace ID, or
	- Producing documentation and scripts for admins to enable the model in your org.

