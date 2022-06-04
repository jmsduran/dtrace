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
from matrix import IdentityMatrix
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


def test_mul_matrix():
    a = Matrix([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 8, 7, 6],
        [5, 4, 3, 2]
    ])

    b = Matrix([
        [-2, 1, 2, 3],
        [3, 2, 1, -1],
        [4, 3, 6, 5],
        [1, 2, 7, 8]
    ])

    c = Matrix([
        [20, 22, 50, 48],
        [44, 54, 114, 108],
        [40, 58, 110, 102],
        [16, 26, 46, 42]
    ])

    assert (a * b) == c


def test_mul_matrix_identity():
    a = Matrix([
        [0, 1, 2, 4],
        [1, 2, 4, 8],
        [2, 4, 8, 16],
        [4, 8, 16, 32]
    ])

    b = IdentityMatrix(4)

    assert (a * b) == a


def test_mul_tuple_identity():
    a = Tuple(1, 2, 3, 4)
    b = IdentityMatrix(4)

    # (a * b) will throw an exception.
    assert (b * a) == a


def test_transpose_matrix():
    a = Matrix([
        [0, 9, 3, 0],
        [9, 8, 0, 8],
        [1, 8, 5, 3],
        [0, 0, 5, 8]
    ])

    b = Matrix([
        [0, 9, 1, 0],
        [9, 8, 8, 0],
        [3, 0, 5, 5],
        [0, 8, 3, 8]
    ])

    a.transpose()

    assert a == b