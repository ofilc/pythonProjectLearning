"""Simple helper to call Anthropic Claude (e.g. Claude Sonnet 3.5).

This module provides a tiny, low-risk wrapper that can be used in
development and tests. It intentionally defers importing `requests`
until a real network call is required so tests can run without
installing HTTP dependencies by using `mock=True`.

Usage:
    from olia_python.llm import generate
    text = generate("Say hello", mock=True)  # returns a deterministic mock response

To use the real Anthropic API set the environment variable
`ANTHROPIC_API_KEY` and call without `mock=True`.
"""
from __future__ import annotations

import os
from typing import Optional

DEFAULT_MODEL = "claude-sonnet-3.5"


def generate(prompt: str, model: Optional[str] = None, max_tokens: int = 300, mock: bool = False) -> str:
    """Generate text from Claude.

    Parameters
    - prompt: text prompt to send
    - model: optional model name (defaults to Claude Sonnet 3.5)
    - max_tokens: maximum tokens to request
    - mock: if True, return a deterministic mock response (no network calls)

    Returns the generated text.

    Raises RuntimeError if a real API call is requested but `ANTHROPIC_API_KEY` is not set.
    """
    if mock:
        return f"MOCK_RESPONSE: {prompt}"

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY not set. Set it in your environment to call the real API.")

    model = model or DEFAULT_MODEL

    # Import requests only when we need to make a network call so tests without requests can still import this module.
    import requests

    url = "https://api.anthropic.com/v1/complete"
    headers = {"x-api-key": api_key, "Content-Type": "application/json"}
    payload = {"model": model, "prompt": prompt, "max_tokens_to_sample": max_tokens}
    resp = requests.post(url, json=payload, headers=headers, timeout=15)
    resp.raise_for_status()
    data = resp.json()

    # Try common response fields used by different Anthropic APIs
    text = data.get("completion") or data.get("output") or data.get("completion_text") or ""
    return text
