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


class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __add__(self, other):
        if isinstance(other, Color):
            red = self.red + other.red
            green = self.green + other.green
            blue = self.blue + other.blue

            return Color(red, green, blue)

        else:
            return None

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.equals(other)

        else:
            return False

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            red = self.red * other
            green = self.green * other
            blue = self.blue * other

            return Color(red, green, blue)

        else:
            return None

    def __ne__(self, other):
        if isinstance(other, Color):
            return not self.equals(other)

        else:
            return True

    def __sub__(self, other):
        if isinstance(other, Color):
            red = self.red - other.red
            green = self.green - other.green
            blue = self.blue - other.blue

            return Color(red, green, blue)

        else:
            return None

    def equals(self, c, **kwargs):
        epsilon = kwargs.get('epsilon', .00001)

        is_r_eq = equals(self.red, c.red, epsilon=epsilon)
        is_g_eq = equals(self.green, c.green, epsilon=epsilon)
        is_b_eq = equals(self.blue, c.blue, epsilon=epsilon)

        return (is_r_eq, is_g_eq, is_b_eq)
