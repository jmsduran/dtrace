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


def test_init():
    c = Color(-0.5, 0.4, 1.7)

    assert c.red == -0.5
    assert c.green == 0.4
    assert c.blue == 1.7


def test_add():
    a = Color(0.9, 0.6, 0.75)
    b = Color(0.7, 0.1, 0.25)
    c = Color(1.6, 0.7, 1.0)

    assert (a + b) == c


def test_equals():
    a = Color(1, 1, 1)
    b = Color(0.99999, 0.99999, 0.99999)
    c = Color(0.9998, 0.9998, 0.9998)

    assert a == b
    assert not (a == 2)
    assert a != c


def test_not_equals():
    a = Color(1, 1, 1)
    b = Color(0, 0, 0)

    assert a != b
    assert a != 2


def test_subtract():
    a = Color(0.9, 0.6, 0.75)
    b = Color(0.7, 0.1, 0.25)
    c = Color(0.2, 0.5, 0.5)

    assert (a - b) == c


def test_multiply():
    a = Color(0.2, 0.3, 0.4)
    b = Color(0.4, 0.6, 0.8)

    assert (a * 2) == b
