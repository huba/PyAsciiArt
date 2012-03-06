#fancy_font.py
#This file is part of the PyAsciiArt project
#Created by Huba Nagy 24.02.12
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

from xml.etree.ElementTree import ElementTree
import text_parser
import os

BUILTINS = {}

abs_path = os.path.abspath(__file__)
abs_path = abs_path.strip("fancyf.py")

builtin_tree = ElementTree()
builtin_tree.parse(abs_path + "BUILTIN_FONTS.xml")
b_fonts = builtin_tree.findall("font")
for child in b_fonts:
    b_font_name_l = list(child.iter("name"))
    b_font_name = text_parser._str_from_list(b_font_name_l)

    b_font_file_l = list(child.iter("file"))
    b_font_file = abs_path + text_parser._str_from_list(b_font_file_l)

    BUILTINS[b_font_name] = b_font_file

class fancy_font:
    def __init__(self, font_name):
        self.font_name = font_name
        self.font_file = BUILTINS[font_name]
        self.font_tree = ElementTree()
        self.font_tree.parse(self.font_file)
        
        self.line_info = 0
        self.uppercase = False
        self.lowercase = False
        self.numbers = False
        self.specials = False
        self.missing_upper = []
        self.missing_lower = []
        self.missing_nums = []
        self.missing_specs = []

        self.characters = {}

        self.get_info()
        self.get_char_map()

    def get_info(self):
        info = self.font_tree.find("info")

        #getting max number of lines making up a character
        line_info = list(info.iter("lines"))
        line_info_s = text_parser._str_from_list(line_info)
        self.line_info = int(line_info_s)

        #getting if there are uppercase characters
        upper_info = list(info.iter("uppercase"))
        self.uppercase = text_parser._is_str_true(upper_info)

        #getting if there are lowercase characters
        lower_info = list(info.iter("lowercase"))
        self.lowercase = text_parser._is_str_true(lower_info)

        #getting if there are numerical characters
        numbr_info = list(info.iter("numbers"))
        self.numbers = text_parser._is_str_true(numbr_info)

        #getting if there are special characters
        specs_info = list(info.iter("specials"))
        self.specials = text_parser._is_str_true(specs_info)

        #getting missing characters
        #TODO get missing characters from xml

    def get_char_map(self):
        space = self.font_tree.findall("space/char/ln")
        spc_cur = []

        for line in space:
            spc_cur.append(line.text)

        self.characters["char_ "] = spc_cur
        
        if self.uppercase:
            uppercase_map = self.font_tree.findall("upper/char")
            for char_map in uppercase_map:
                char_id = text_parser._str_from_list(list(char_map.iter("char_id")))
                char_lns = list(char_map.iter("ln"))
                char_cur = []

                for line in char_lns:
                    char_cur.append(line.text)

                self.characters[char_id] = char_cur

        if self.lowercase:
            lowercase_map = self.font_tree.findall("lower/char")
            for char_map in lowercase_map:
                char_id = text_parser._str_from_list(list(char_map.iter("char_id")))
                char_lns = list(char_map.iter("ln"))
                char_cur = []

                for line in char_lns:
                    char_cur.append(line.text)

                self.characters[char_id] = char_cur

        if self.numbers:
            numbers_map = self.font_tree.findall("nums/char")
            for char_map in numbers_map:
                char_id = text_parser._str_from_list(list(char_map.iter("char_id")))
                char_lns = list(char_map.iter("ln"))
                char_cur = []

                for line in char_lns:
                    char_cur.append(line.text)

                self.characters[char_id] = char_cur

        if self.specials:
            specials_map = self.font_tree.findall("spec/char")
            for char_map in specials_map:
                char_id = text_parser._str_from_list(list(char_map.iter("char_id")))
                char_lns = list(char_map.iter("ln"))
                char_cur = []

                for line in char_lns:
                    char_cur.append(line.text)

                self.characters[char_id] = char_cur
                    
    def get_induvidual_char_map(self, lines_list):
        output = []
        for line in lines_list:
            output.append(line.text)

        return output
