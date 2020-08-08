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
