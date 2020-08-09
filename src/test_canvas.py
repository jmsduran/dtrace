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

from canvas import Canvas
from color import Color
import pytest


def test_create():
    c = Canvas(10, 20)
    color_black = Color(0, 0, 0)

    assert c is not None
    assert c.width == 10
    assert c.height == 20

    for x in range(c.width):
        for y in range(c.height):
            assert c.pixel_at(x, y) == color_black


def test_read_write_pixel():
    c = Canvas(10, 20)
    color_red = Color(1, 0, 0)
    c.write_pixel(2, 3, color_red)

    assert c.pixel_at(2, 3) == color_red


def test_out_of_bounds_errors():
    c = Canvas(10, 20)

    with pytest.raises(IndexError):
        c.pixel_at(10, 20)

    with pytest.raises(IndexError):
        c.pixel_at(-1, -1)

    with pytest.raises(IndexError):
        c.pixel_at(9, 20)

    with pytest.raises(IndexError):
        c.pixel_at(10, 19)

    with pytest.raises(IndexError):
        c.write_pixel(10, 20, Color(0, 0, 0))

    with pytest.raises(IndexError):
        c.write_pixel(-1, -1, Color(0, 0, 0))

    with pytest.raises(IndexError):
        c.write_pixel(9, 20, Color(0, 0, 0))

    with pytest.raises(IndexError):
        c.write_pixel(10, 19, Color(0, 0, 0))
