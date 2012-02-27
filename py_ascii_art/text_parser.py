#text_parser.py
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

from xml.etree.ElementTree import ElementTree

def parse_str(text_i):
    string = ""
    for line in text_i:
        string += line

    original = list(string)
    new = []
    i = 0
    while i < len(original) - 1:
        n = ""
        n = original[i] + original[i + 1]
        new.append(n)
        i += 1

    x = 0
    parsed = []
    row = ""
    while x < len(original):
        if x < len(new):
            if new[x] == "&N":
                if x > 0:
                    if new[x - 1] != "&&":
                        parsed.append(row)
                        row = ""
                        x += 2

                    else:
                        x += 1

                else:
                    parsed.append(row)
                    row = ""
                    x += 2

            elif new[x] == "&T":
                if x > 0:
                    if new[x - 1] != "&&":
                        row += (" ") * 4
                        x += 2

                    else:
                        x += 1

                else:
                    row += (" ") * 4
                    x += 2

            else:
                row += original[x]
                x += 1
                
        else:
            row += original[x]
            x += 1

    parsed.append(row)
    return parsed

def parse_to_width(text_i, max_width):
    string = ""
    for line in text_i:
        string += line
        
    original = list(string)
    new = []
    i = 0
    while i < len(original) - 1:
        n = ""
        n = original[i] + original[i + 1]
        new.append(n)
        i += 1

    x = 0
    parsed = []
    row = ""
    cur_width = 0
    while x < len(original):
        if cur_width == max_width:
            parsed.append(row)
            row = ""
            cur_width = 0
            
        if x < len(new):
            if new[x] == "&N":
                if x > 0:
                    if new[x - 1] != "&&":
                        parsed.append(row)
                        row = ""
                        x += 2
                        cur_width = 0

                    else:
                        x += 1
                        cur_width += 1

                else:
                    parsed.append(row)
                    row = ""
                    x += 2
                    cur_width = 0

            elif new[x] == "&T":
                if x > 0:
                    if new[x - 1] != "&&":
                        row += (" ") * (4 - cur_width % 4)
                        x += 2
                        cur_width += (4 - cur_width % 4)

                    else:
                        x += 1
                        cur_width += 1

                else:
                    row += (" ") * (4 - cur_width % 4)
                    x += 2
                    cur_width += (4 - cur_width % 4)

            else:
                row += original[x]
                x += 1
                cur_width += 1
                
        else:
            row += original[x]
            x += 1
            cur_width += 1

    parsed.append(row)
    return parsed

def is_str_true(list_i):
    output = False
    info_s = str_from_list(list_i)

    if info_s.upper() == "TRUE":
        output = True
    else:
        output = False

    return output

def str_from_list(list_i):
    str_o = ""

    for char in list_i:
        str_o += char.text

    return str_o
