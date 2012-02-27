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
                 frame_width = 1, side_fr = True):
        self.filler = filler
        self.holder = holder
        self.text = text_i
        self.width = width
        self.frame_width = frame_width
        self.side_fr = side_fr
        self.art = ""
        
        self.change_text(self.text)

    def change_text(self, text):
        self.parsed_text = text_parser.parse_to_width(text, (self.width - 2 * self.frame_width))
        self.art = self.gen_framed_text()
        
    def change_width(self, width):
        self.width = width
        self.chang_text(self.text)

    def change_frame_width(self, frame_width):
        self.frame_width = frame_width
        self.change_text(self.text)

    def set_side_frame(self, side_fr):
        self.side_fr = side_fr
        self.change_text(self.text)
        
    def gen_framed_text(self):
        output = ""
        row_count = 0
        col_count = 0
        row = []
        total_rows = len(self.parsed_text)
        if self.side_fr:
            total_cols = self.width - (2 * self.frame_width)
        else:
            total_cols = self.width

        output = output + ((self.filler * self.width) + "\n") * self.frame_width
        while row_count < total_rows:
            col_count = 0
            if self.side_fr:
                output = output + (self.filler * self.frame_width)
                
            row = self.parsed_text[row_count]
            chars = list(row)
            while col_count <= total_cols:
                if col_count < len(row):
                    if row[col_count] == " ":
                        output = output + self.holder
                    else:
                        output = output + row[col_count]
                elif col_count > len(row):
                    output = output + self.holder

                col_count = col_count + 1

            if self.side_fr:
                output = output + (self.filler * self.frame_width)

            output = output + "\n"
            row_count = row_count + 1
            
        output = output + ((self.filler * self.width) + "\n") *self.frame_width
        return output

    def print_art(self):
        print self.art
