#text_frame.py
#This file is part of the PyAsciiArt project
#Created by Huba Nagy 22.02.12
#  and is released under the MIT Licence.
#
#Copyright (c) 2012 Huba Z. Nagy
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import text_parser

class framed_text:
    def __init__(self, text_i, filler = "*", holder = " ", width = 40,
                 frame_width = 1, side_filler = None,
                 side_fr = True, title = None):
        self.set_text(text_i, False)
        self.set_filler(filler, False)
        self.set_holder(holder, False)
        self.set_width(width, False)
        self.set_frame_width(frame_width, False)
        self.set_side_frame(side_fr, side_filler, False)
        self.set_title(title)
        
        self.set_text(self._text)

    def set_text(self, text, regen = True):
        self._text = text
        if regen:
            self._parsed_text = text_parser._parse_str(text, width = (self._width - 2 * self._frame_width))
            self._art = self._gen_framed_text()
        
    def set_width(self, width, regen = True):
        self._width = width
        if regen:
            self.set_text(self._text)

    def set_frame_width(self, frame_width, regen = True):
        self._frame_width = frame_width
        if regen:
            self.set_text(self._text)

    def set_title(self, title, regen = True):
        self._title = title
        if title:
            self._frame_title = True

        else:
            self._frame_title = False
            
        if regen:
            self.set_text(self._text)

    def set_filler(self, filler, regen = True):
        if filler:
            self._filler = filler
            if regen:
                self.set_text(self._text)

    def set_holder(self, holder, regen = True):
        if holder:
            self._holder = holder
            if regen:
                self.set_text(self._text)

    def set_side_frame(self, side_fr = True, side_filler = None, regen = True):
        self._side_fr = side_fr

        if side_fr:
            if side_filler:
                self._side_filler = side_filler

            else:
                self._side_filler = self._filler

        if regen:
            self.set_text(self._text)
        
    def _gen_framed_text(self):
        output = ""
        row_count = 0
        col_count = 0
        row = []
        total_rows = len(self._parsed_text)
        if self._side_fr:
            total_cols = self._width - (2 * self._frame_width)
        else:
            total_cols = self._width

        if self._title:
            if self._frame_title:
                output += ((self._filler * self._width) + "\n") 

            title = text_parser._center(self._width, self._title)
            for r in title:
                row_str = ""
                prev_ch = None
                for ch in r:
                    if ch == " ":
                        row_str += self._filler
                        
                    else:
                        row_str += ch

                output += row_str + "\n"

            if self._frame_title:
                output += ((self._filler * self._width) + "\n") 

        else:
            output += ((self._filler * self._width) + "\n") * self._frame_width
            
        while row_count < total_rows:
            col_count = 0
            if self._side_fr:
                output += (self._side_filler * self._frame_width)
                
            row = self._parsed_text[row_count]
            chars = list(row)
            while col_count <= total_cols:
                if col_count < len(row):
                    if row[col_count] == " ":
                        output += self._holder
                    else:
                        output += row[col_count]
                elif col_count > len(row):
                    output += self._holder

                col_count += 1

            if self._side_fr:
                output += (self._side_filler * self._frame_width)

            output += "\n"
            row_count += 1
            
        output = output + ((self._filler * self._width) + "\n") *self._frame_width
        return output

    def print_art(self):
        print self._art
