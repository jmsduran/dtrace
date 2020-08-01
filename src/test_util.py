from util import equals

def test_equals():
    a = -1.000009
    b = -1

    assert equals(a, b)

def test_equals_override_epsilon():
    a = 1.0019
    b = 1

    assert equals(a, b, epsilon=.002)

def test_not_equals():
    a = 1.00001
    b = 1

    assert not equals(a, b)

def test_not_equals_override_epsilon():
    a = -1.002
    b = -1

    assert not equals(a, b, epsilon=.002)

