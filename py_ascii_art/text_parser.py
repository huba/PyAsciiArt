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

def parse_str(input_s):
    chars = list(input_s)
    input_S = input_s.upper()
    CHARS = list(input_S)
    row_s = ""
    char_count = 0
    output = []
    first = True

    while char_count < len(chars):
        prev = char_count - 1
        nxt = char_count + 1
        if chars[char_count] == "\\" :
            if char_count < (len(chars) - 1):
                if CHARS[nxt] == "N":
                    if char_count > 0:
                        if chars[prev] != "\\":
                                output.append(row_s)
                                row_s = ""
                                first = False
                                char_count = char_count + 1

                    else:
                        output.append(row_s)
                        row_s = ""
                        first = False
                        char_count = char_count + 1

                elif CHARS[nxt] == "T":
                    if char_count > 0:
                        if chars[prev] != "\\":
                                row_s = row_s + (" " * 4)
                                char_count = char_count + 1

                    else:
                        row_s = row_s + (" " * 4)
                        char_count = char_count + 1

                else:
                    row_s = row_s + chars[char_count]

            else:
                row_s = row_s + chars[char_count]

        else:
            row_s = row_s + chars[char_count]

        char_count = char_count + 1

    output.append(row_s)
    return output
