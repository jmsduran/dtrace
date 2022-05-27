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
        if isinstance(other, Tuple):
            b = [other.x, other.y, other.z, other.w]
            c = [0] * 4

            for row in range(0, 4):
                for col in range(0, 4):
                    c[row] += (self.at(row, col) * b[col])

            return Tuple(c[0], c[1], c[2], c[3])

        elif isinstance(other, Matrix):
            return None

        else:
            return None

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
