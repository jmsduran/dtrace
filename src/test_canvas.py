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


def test_create_fill_color():
    color_green = Color(0, 1, 0)
    c = Canvas(10, 20, fill_color=color_green)

    assert c is not None
    assert c.width == 10
    assert c.height == 20

    for x in range(c.width):
        for y in range(c.height):
            assert c.pixel_at(x, y) == color_green


def test_read_write_pixel():
    c = Canvas(10, 20)
    color_red = Color(1, 0, 0)
    c.write_pixel(2, 3, color_red)

    assert c.pixel_at(2, 3) == color_red


def test_to_ppm_str_eof():
    c = Canvas(5, 3)
    ppm_str = c.to_ppm_str()

    assert ppm_str[-1] == '\n'


def test_to_ppm_str_metadata():
    c = Canvas(5, 3)

    ppm_str = c.to_ppm_str()
    ppm_str_list = ppm_str.splitlines()

    expected_str_list = """P3
5 3
255
""".splitlines()

    for i in range(3):
        assert ppm_str_list[i] == expected_str_list[i]


@pytest.mark.skip(reason="Not implemented yet")
def test_to_ppm_str_long_lines():
    c = Canvas(10, 2, fill_color=Color(1, 0.8, 0.6))

    ppm_str = c.to_ppm_str()
    ppm_str_list = ppm_str.splitlines()

    expected_str_list = """255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204​
153 255 204 153 255 204 153 255 204 153 255 204 153​
255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204​
153 255 204 153 255 204 153 255 204 153 255 204 153
""".splitlines()

    for i in range(3, 7):
        assert ppm_str_list[i] == expected_str_list[i - 3]


@pytest.mark.skip(reason="Not implemented yet")
def test_to_ppm_str_pixels():
    c = Canvas(5, 3)
    c.write_pixel(0, 0, Color(1.5, 0, 0))
    c.write_pixel(2, 1, Color(0, 0.5, 0))
    c.write_pixel(4, 2, Color(-0.5, 0, 1))

    ppm_str = c.to_ppm_str()
    ppm_str_list = ppm_str.splitlines()

    expected_str_list = """255 0 0 0 0 0 0 0 0 0 0 0 0 0 0​
​0 0 0 0 0 0 0 128 0 0 0 0 0 0 0​
​0 0 0 0 0 0 0 0 0 0 0 0 0 0 255
""".splitlines()

    for i in range(3, 6):
        assert ppm_str_list[i] == expected_str_list[i - 3]


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
