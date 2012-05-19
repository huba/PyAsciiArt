#titles.py
#This file is part of the PyAsciiArt project
#Created by Huba Nagy 17.02.12
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


import font
import fancyf
import text_parser

class plain_title:
    def __init__(self, text):
        self.change_text(text)

    def change_text(self, text):
        self.art = ""
        rows_content = text_parser._parse_str(text)
        row = 0
        while row < len(rows_content):
            self.art = self.art + self.gen_ascii_art(rows_content[row])
            row = row + 1
        
    def gen_ascii_art(self, input_s):
        input_s = input_s.upper()
        chars = list(input_s)
        row = 0
        output = ""

        while row <= 7:
            for char in input_s:
                output += font.FONT_MAP[char][row]

            output = output + "\n"
            row = row + 1
            char_number = 0
            
        return output

    def print_art(self):
        print self.art

class fancy_title:
    def __init__(self, text, ffont):
        self.font = ffont
        self.text = text
        self.change_text(self.text)

    def change_text(self, text):
        self.art = ""
        rows_content = text_parser.parse_str(text)
        row = 0
        while row < len(rows_content):
            self.art = self.art + self.gen_ascii_art(rows_content[row])
            row = row + 1

    def change_font(self, ffont):
        self.font = ffont
        self.change_text(self.text)
        
    def gen_ascii_art(self, input_s):
        if self.font.uppercase:
            if self.font.lowercase:
                input_s = input_s
            else:
                input_s = input_s.upper()
        else:
            if self.font.uppercase:
                input_s = input_s
            else:
                input_s = input_s.lower()
                
        chars = list(input_s)
        row = 0
        char_number = 0
        output = ""

        while row < self.font.line_info:
            while char_number < len(chars):
                char = chars[char_number]
                char_id = "char_" + char
                if char_id in self.font.characters:
                    output += self.font.characters[char_id][row]
                else:
                    output += self.font.characters["char_ "][row]

                char_number += 1

            output += "\n"
            row += 1
            char_number = 0
            
        return output

    def print_art(self):
        print self.art

def test():
    ff = fancyf.fancy_font("F3D_NE")
    ft = fancy_title("BRi&NHIyz&NHuba&N x8&NLinux&Nh%o", ff)
    pt = plain_title("Hi")
    ft.print_art()
    pt.print_art()

