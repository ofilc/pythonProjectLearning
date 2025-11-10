from olia_python.llm import generate


def test_generate_mock():
    out = generate("Hello world", mock=True)
    assert out.startswith("MOCK_RESPONSE")
