from color import Color


class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = []

        for x in range(self.width):
            self.pixels.append([])
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
