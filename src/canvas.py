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

from color import Color


class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = []

        for x in range(self.width):
            self.pixels.append([])

            # pylint: disable=unused-variable
            for y in range(self.height):
                self.pixels[x].append(Color(0, 0, 0))

    def _validate_pixel_range(self, x, y):
        if not ((0 <= x < self.width) and (0 <= y < self.height)):
            raise IndexError

    def pixel_at(self, x, y):
        self._validate_pixel_range(x, y)

        return self.pixels[x][y]

    def write_pixel(self, x, y, color):
        self._validate_pixel_range(x, y)

        self.pixels[x][y] = color
