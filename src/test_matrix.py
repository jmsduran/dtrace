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
from matrix import Matrix


def _assert_matrix(m, data):
    i = 0

    for row in range(0, m.row_len()):
        for col in range(0, m.col_len()):
            assert m.at(row, col) == data[row][col]
            i += 1

    assert i == m.element_count()


def test_init():
    a_data = [
        [1, 2, 3, 4],
        [5.5, 6.5, 7.5, 8.5],
        [9, 10, 11, 12],
        [13.5, 14.5, 15.5, 16.5]
    ]

    b_data = [
        [-3, 5],
        [1, -2]
    ]

    c_data = [
        [-3, 5, 0],
        [1, -2, -7],
        [0, 1, 1]
    ]

    a = Matrix(a_data)
    b = Matrix(b_data)
    c = Matrix(c_data)

    _assert_matrix(a, a_data)
    _assert_matrix(b, b_data)
    _assert_matrix(c, c_data)


def test_equals():
    a = Matrix([
        [-3, 5],
        [1, -2]
    ])

    b = Matrix([
        [-3, 5],
        [1, -2]
    ])

    c = Matrix([
        [-3, 5],
        [1, -3]
    ])

    assert a == b
    assert a != c
    assert a != 2


def test_mul_tuple():
    a = Matrix([
        [1, 2, 3, 4],
        [2, 4, 4, 2],
        [8, 6, 4, 1],
        [0, 0, 0, 1]
    ])

    b = Tuple(1, 2, 3, 1)

    assert (a * b) == Tuple(18, 24, 33, 1)
