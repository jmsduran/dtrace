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


def test_equals():
    a = -1.000009
    b = -1

    assert equals(a, b)


def test_equals_override_epsilon():
    a = 1.0019
    b = 1

    assert equals(a, b, epsilon=.002)


def test_equals_override_epsilon_zero():
    a = 1
    b = 1

    assert equals(a, b, epsilon=0)


def test_not_equals():
    a = 1.00001
    b = 1

    assert not equals(a, b)


def test_not_equals_override_epsilon():
    a = -1.002
    b = -1

    assert not equals(a, b, epsilon=.002)
