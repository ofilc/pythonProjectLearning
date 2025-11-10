from olia_python.main import greet


def test_greet():
    assert greet() == "Hello, olia_python"
