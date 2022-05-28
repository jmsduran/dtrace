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


class Matrix:
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented

        return self.equals(other)

    def __mul__(self, other):
        # Only supports 4x4 matrix to 1x4 tuple multiplication
        if self._is_tuple_mul(other):
            return self._tuple_mul(other)

        # Only supports square matrix multiplication of equal sizes
        elif self._is_square_matrix_mul(other):
            return self._square_matrix_mul(other)

        else:
            return None

    def _is_tuple_mul(self, other):
        return (isinstance(other, Tuple) and
                self.row_len() == 4 and
                self.col_len() == 4)

    def _tuple_mul(self, other):
        b = [other.x, other.y, other.z, other.w]
        c = [0] * 4

        for row in range(0, 4):
            for col in range(0, 4):
                c[row] += (self.at(row, col) * b[col])

        return Tuple(c[0], c[1], c[2], c[3])

    def _is_square_matrix_mul(self, other):
        return (isinstance(other, Matrix) and
                self.row_len() == other.row_len() and
                self.col_len() == other.col_len() and
                self.col_len() == other.row_len())

    def _square_matrix_mul(self, other):
        c = [[0 for _ in range(4)] for _ in range(4)]

        for row in range(0, self.row_len()):
            for col in range(0, self.col_len()):
                for j in range(0, self.col_len()):
                    c[row][col] += self.at(row, j) * other.at(j, col)

        return Matrix(c)

    def equals(self, m):
        for row in range(0, m.row_len()):
            for col in range(0, m.col_len()):
                if self.at(row, col) != m.at(row, col):
                    return False

        if self.element_count() != m.element_count():
            return False

        return True

    def at(self, row, col):
        return self.data[row][col]

    def row_len(self):
        return len(self.data)

    def col_len(self):
        return len(self.data[0])

    def element_count(self):
        return self.col_len() * self.row_len()


class IdentityMatrix(Matrix):
    def __init__(self, size):
        self.data = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(0, size):
            self.data[i][i] = 1
