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
import math


class Canvas:
    def __init__(self, width, height, **kwargs):
        fill_color = kwargs.get('fill_color', Color(0, 0, 0))
        self.color_scale = kwargs.get('color_scale', 255)
        self.ppm_max_char_line = kwargs.get('ppm_max_char_line', 70)

        self.width = width
        self.height = height
        self.pixels = []

        for y in range(self.height):
            self.pixels.append([])

            # pylint: disable=unused-variable
            for x in range(self.width):
                self.pixels[y].append(fill_color)

    def _append_space_if_less_than(self, a, b, char_list):
        if a < b:
            char_list.append(' ')

    def _format_row_max_line(self, char_list):
        ind_offset = 0
        char_ind = 0

        while (ind_offset + char_ind) < len(char_list):
            if char_ind >= (self.ppm_max_char_line - 1):
                while char_list[ind_offset + char_ind] != ' ':
                    char_ind -= 1

                char_list[ind_offset + char_ind] = '\n'
                ind_offset += char_ind
                char_ind = 0

            else:
                char_ind += 1

        char_list.append('\n')

    def _get_rgb_char_list(self, pixel):
        max_color = self.color_scale
        rgb = [pixel.red, pixel.green, pixel.blue]
        rgb_len = len(rgb)
        char_list = []

        for i in range(rgb_len):
            adj_color = math.ceil(rgb[i] * max_color)
            adj_color = max_color if adj_color > max_color else adj_color
            adj_color = 0 if adj_color < 0 else adj_color

            char_list += list(str(adj_color))
            self._append_space_if_less_than(i, rgb_len - 1, char_list)

        return char_list

    def _create_ppm_body(self):
        ppm_body_str = ''

        for y in range(self.height):
            pixel_row_char_list = []

            for x in range(self.width):
                pixel = self.pixel_at(x, y)
                pixel_row_char_list += self._get_rgb_char_list(pixel)

                self._append_space_if_less_than(x, self.width - 1,
                                                pixel_row_char_list)

            self._format_row_max_line(pixel_row_char_list)
            ppm_body_str += ''.join(pixel_row_char_list)

        return ppm_body_str

    def _create_ppm_header(self):
        return """P3
{0} {1}
{2}
""".format(self.width, self.height, self.color_scale)

    def _validate_pixel_range(self, x, y):
        if not ((0 <= x < self.width) and (0 <= y < self.height)):
            raise IndexError

    def pixel_at(self, x, y):
        self._validate_pixel_range(x, y)

        return self.pixels[y][x]

    def to_ppm_str(self):
        ppm_header = self._create_ppm_header()
        ppm_body = self._create_ppm_body()

        return ppm_header + ppm_body

    def to_ppm(self):
        ppm_str = self.to_ppm_str()

        with open('./', 'w') as ppm_file:
            ppm_file.write(ppm_str)

    def write_pixel(self, x, y, color):
        self._validate_pixel_range(x, y)

        self.pixels[y][x] = color
