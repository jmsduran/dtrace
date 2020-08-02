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
from util import equals


class Tuple:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        w = self.w + other.w

        return Tuple(x, y, z, w)

    def __eq__(self, other):
        if isinstance(other, Tuple):
            return self.equals(other)

        else:
            return False

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x = self.x * other
            y = self.y * other
            z = self.z * other
            w = self.w * other

            return Tuple(x, y, z, w)

        else:
            return None

    def __ne__(self, other):
        if isinstance(other, Tuple):
            return not self.equals(other)

        else:
            return True

    def __neg__(self):
        return self.negate()

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        w = self.w - other.w

        return Tuple(x, y, z, w)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            x = self.x / other
            y = self.y / other
            z = self.z / other
            w = self.w / other

            return Tuple(x, y, z, w)

        else:
            return None

    def cross_product(self, t):
        return Tuple(self.y * t.z - self.z * t.y,
                     self.z * t.x - self.x * t.z,
                     self.x * t.y - self.y * t.x, 0)

    def dot_product(self, t):
        return self.x * t.x + self.y * t.y + self.z * t.z + self.w * t.w

    def equals(self, t, **kwargs):
        epsilon = kwargs.get('epsilon', .00001)

        is_x_equal = equals(self.x, t.x, epsilon=epsilon)
        is_y_equal = equals(self.y, t.y, epsilon=epsilon)
        is_z_equal = equals(self.z, t.z, epsilon=epsilon)
        is_w_equal = equals(self.w, t.w, epsilon=epsilon)

        return (is_x_equal and is_y_equal and is_z_equal and is_w_equal)

    def is_point(self):
        return True if equals(self.w, 1) else False

    def is_vector(self):
        return True if equals(self.w, 0) else False

    def magnitude(self):
        x_sq = self.x ** 2
        y_sq = self.y ** 2
        z_sq = self.z ** 2
        w_sq = self.w ** 2

        return sqrt(x_sq + y_sq + z_sq + w_sq)

    def normalize(self):
        magnitude = self.magnitude()

        return self / magnitude

    def negate(self):
        return Tuple(0, 0, 0, 0) - self
