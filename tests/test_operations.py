from mathquiz.operations import OPERATIONS

def test_add():
    assert OPERATIONS['+'].apply(3.5, 2) == 5.5

def test_subtract():
    assert OPERATIONS['-'].apply(3, 2) == 1

def test_multiply():
    assert OPERATIONS['*'].apply(4.5, 2) == 9.0

def test_divide():
    assert OPERATIONS['/'].apply(6, 2) == 3
    assert OPERATIONS['/'].apply(6, 0) == float('inf')