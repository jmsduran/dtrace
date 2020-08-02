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
        return self.equals(other)

    def __ne__(self, other):
        return not self.equals(other)

    def __neg__(self):
        return self.negate()

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        w = self.w - other.w

        return Tuple(x, y, z, w)

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

    def negate(self):
        return Tuple(0, 0, 0, 0) - self
