from tuple import is_point
from tuple import is_vector
from tuple import Tuple

def test_tuple_point_float():
    t = Tuple(4.3, -4.2, 3.1, 1.0)
    
    assert t.x == 4.3
    assert t.y == -4.2
    assert t.z == 3.1
    assert t.w == 1.0

    assert is_point(t)
    assert not is_vector(t)

def test_tuple_point_int():
    t = Tuple(4, -4, 3, 1)

    assert t.x == 4
    assert t.y == -4
    assert t.z == 3
    assert t.w == 1

    assert is_point(t)
    assert not is_vector(t)

def test_tuple_vector_float():
    t = Tuple(4.3, -4.2, 3.1, 0.0)

    assert t.x == 4.3
    assert t.y == -4.2
    assert t.z == 3.1
    assert t.w == 0.0

    assert not is_point(t)
    assert is_vector(t)

def test_tuple_vector_int():
    t = Tuple(4, -4, 3, 0)

    assert t.x == 4
    assert t.y == -4
    assert t.z == 3
    assert t.w == 0

    assert not is_point(t)
    assert is_vector(t)

