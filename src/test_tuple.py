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

from tuple import Tuple


def test_tuple_add():
    a = Tuple(3, -2, 5, 1)
    b = Tuple(-2, 3, 1, 0)

    assert (a + b) == Tuple(1, 1, 6, 1)


def test_tuple_equals():
    a = Tuple(2, 3, 1, 1)
    b = Tuple(2, 3, 1.000009, 1)

    assert a.equals(b)
    assert a == b


def test_tuple_equals_override_epsilon():
    a = Tuple(2, 3, 1, 0)
    b = Tuple(2, 3, 1, 0)

    assert a.equals(b, epsilon=0)


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
