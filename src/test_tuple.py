# dtrace - Python ray tracer
# Copyright (C) 2020 James Duran
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from math import sqrt
from tuple import Tuple


def test_tuple_add():
    a = Tuple(3, -2, 5, 1)
    b = Tuple(-2, 3, 1, 0)

    assert (a + b) == Tuple(1, 1, 6, 1)


def test_tuple_div():
    a = Tuple(1, 2, 3, 4)
    b = Tuple(2, 3, 4, 5)

    assert (a / b) is None


def test_tuple_mult():
    a = Tuple(1, 2, 3, 4)
    b = Tuple(2, 3, 4, 5)

    assert (a * b) is None


def test_tuple_negate():
    a = Tuple(1, -2, 3, -4)
    expected = Tuple(-1, 2, -3, 4)

    assert -a == expected
    assert a.negate() == expected


def test_tuple_scalar_mult():
    a = Tuple(1, -2, 3, -4)

    assert a * 3.5 == Tuple(3.5, -7, 10.5, -14)


def test_tuple_scalar_div():
    a = Tuple(1, -2, 3, -4)

    assert a / 2 == Tuple(0.5, -1, 1.5, -2)


def test_tuple_subtract_points():
    a = Tuple(3, 2, 1, 1)
    b = Tuple(5, 6, 7, 1)

    c = a - b

    assert c.is_vector()
    assert c == Tuple(-2, -4, -6, 0)


def test_tuple_subtract_vector_from_point():
    a = Tuple(3, 2, 1, 1)
    b = Tuple(5, 6, 7, 0)

    c = a - b

    assert c.is_point()
    assert c == Tuple(-2, -4, -6, 1)


def test_tuple_subtract_vectors():
    a = Tuple(3, 2, 1, 0)
    b = Tuple(5, 6, 7, 0)

    c = a - b

    assert c.is_vector()
    assert c == Tuple(-2, -4, -6, 0)


def test_tuple_equals():
    a = Tuple(2, 3, 1, 1)
    b = Tuple(2, 3, 1.000009, 1)

    assert a.equals(b)
    assert a == b


def test_tuple_equals_override_epsilon():
    a = Tuple(2, 3, 1, 0)
    b = Tuple(2, 3, 1, 0)

    assert a.equals(b, epsilon=0)


def test_tuple_magnitude():
    a = Tuple(1, 0, 0, 0)

    assert a.is_vector()
    assert a.magnitude() == 1

    b = Tuple(0, 1, 0, 0)

    assert b.is_vector()
    assert b.magnitude() == 1

    c = Tuple(0, 0, 1, 0)

    assert c.is_vector()
    assert c.magnitude() == 1

    d = Tuple(1, 2, 3, 0)

    assert d.is_vector()
    assert d.magnitude() == sqrt(14)

    e = Tuple(-1, -2, -3, 0)

    assert e.is_vector()
    assert e.magnitude() == sqrt(14)


def test_tuple_normalize():
    a = Tuple(4, 0, 0, 0)

    assert a.is_vector()
    assert a.normalize() == Tuple(1, 0, 0, 0)

    b = Tuple(1, 2, 3, 0)
    b_normalize = b.normalize()

    assert b.is_vector()
    assert b_normalize == Tuple(0.26726, 0.53452, 0.80178, 0)
    assert b_normalize.magnitude() == 1


def test_tuple_not_equals():
    a = Tuple(2, 3, 1, 1)
    b = Tuple(2, 3.00001, 1, 1)

    assert not a.equals(b)
    assert a != b


def test_tuple_not_equals_override_epsilon():
    a = Tuple(2, 3, 1, 0)
    b = Tuple(2.000009, 3, 1, 0)

    assert not a.equals(b, epsilon=0)


def test_tuple_point_float():
    t = Tuple(4.3, -4.2, 3.1, 1.0)

    assert t.x == 4.3
    assert t.y == -4.2
    assert t.z == 3.1
    assert t.w == 1.0

    assert t.is_point()
    assert not t.is_vector()


def test_tuple_point_int():
    t = Tuple(4, -4, 3, 1)

    assert t.x == 4
    assert t.y == -4
    assert t.z == 3
    assert t.w == 1

    assert t.is_point()
    assert not t.is_vector()


def test_tuple_vector_float():
    t = Tuple(4.3, -4.2, 3.1, 0.0)

    assert t.x == 4.3
    assert t.y == -4.2
    assert t.z == 3.1
    assert t.w == 0.0

    assert not t.is_point()
    assert t.is_vector()


def test_tuple_vector_int():
    t = Tuple(4, -4, 3, 0)

    assert t.x == 4
    assert t.y == -4
    assert t.z == 3
    assert t.w == 0

    assert not t.is_point()
    assert t.is_vector()
