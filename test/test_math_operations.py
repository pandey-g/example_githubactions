from src.math_operations import add, sub

def test_add(a, b):
    assert add(a, b) == a + b

def test_sub(a, b):
    assert sub(a, b) == a - b