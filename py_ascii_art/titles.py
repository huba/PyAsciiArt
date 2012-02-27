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
        rows_content = text_parser.parse_str(text)
        row = 0
        while row < len(rows_content):
            self.art = self.art + self.gen_ascii_art(rows_content[row])
            row = row + 1
        
    def gen_ascii_art(self, input_s):
        input_s = input_s.upper()
        chars = list(input_s)
        row = 0
        char_number = 0
        output = ""

        while row <= 7:
            while char_number < len(chars):
                char = chars[char_number]
                if char == "A":
                    output = output + font.char_A[row]

                elif char == "B":
                    output = output + font.char_B[row]
                    
                elif char == "C":
                    output = output + font.char_C[row]

                elif char == "D":
                    output = output + font.char_D[row]

                elif char == "E":
                    output = output + font.char_E[row]

                elif char == "F":
                    output = output + font.char_F[row]

                elif char == "G":
                    output = output + font.char_G[row]

                elif char == "H":
                    output = output + font.char_H[row]

                elif char == "I":
                    output = output + font.char_I[row]

                elif char == "J":
                    output = output + font.char_J[row]

                elif char == "K":
                    output = output + font.char_K[row]

                elif char == "L":
                    output = output + font.char_L[row]

                elif char == "M":
                    output = output + font.char_M[row]

                elif char == "N":
                    output = output + font.char_N[row]

                elif char == "O":
                    output = output + font.char_O[row]

                elif char == "P":
                    output = output + font.char_P[row]

                elif char == "Q":
                    output = output + font.char_Q[row]

                elif char == "R":
                    output = output + font.char_R[row]

                elif char == "S":
                    output = output + font.char_S[row]

                elif char == "T":
                    output = output + font.char_T[row]

                elif char == "U":
                    output = output + font.char_U[row]

                elif char == "V":
                    output = output + font.char_V[row]

                elif char == "W":
                    output = output + font.char_W[row]

                elif char == "X":
                    output = output + font.char_X[row]

                elif char == "Y":
                    output = output + font.char_Y[row]

                elif char == "Z":
                    output = output + font.char_Z[row]

                elif char == " ":
                    output = output + font.char_space[row]

                elif char == "0":
                    output = output + font.char_0[row]

                elif char == "1":
                    output = output + font.char_1[row]

                elif char == "2":
                    output = output + font.char_2[row]

                elif char == "3":
                    output = output + font.char_3[row]

                elif char == "4":
                    output = output + font.char_4[row]

                elif char == "5":
                    output = output + font.char_5[row]

                elif char == "6":
                    output = output + font.char_6[row]

                elif char == "7":
                    output = output + font.char_7[row]

                elif char == "8":
                    output = output + font.char_8[row]

                elif char == "9":
                    output = output + font.char_9[row]

                elif char == "-":
                    output = output + font.char_dash[row]

                elif char == "_":
                    output = output + font.char_uscr[row]

                elif char == "=":
                    output = output + font.char_equa[row]

                elif char == "+":
                    output = output + font.char_plus[row]

                elif char == ".":
                    output = output + font.char_fstp[row]

                elif char == ",":
                    output = output + font.char_comm[row]

                elif char == ":":
                    output = output + font.char_colo[row]

                elif char == ";":
                    output = output + font.char_seco[row]

                elif char == "!":
                    output = output + font.char_excl[row]

                elif char == "?":
                    output = output + font.char_ques[row]

                elif char == "%":
                    output = output + font.char_perc[row]

                elif char == "@":
                    output = output + font.char_atsg[row]

                elif char == ">":
                    output = output + font.char_gulc[row]

                elif char == "<":
                    output = output + font.char_gulo[row]

                elif char == "#":
                    output = output + font.char_hash[row]

                elif char == "*":
                    output = output + font.char_star[row]

                elif char == ")":
                    output = output + font.char_brcc[row]

                elif char == "(":
                    output = output + font.char_brco[row]

                elif char == "]":
                    output = output + font.char_sqbc[row]

                elif char == "[":
                    output = output + font.char_sqbo[row]

                elif char == "}":
                    output = output + font.char_crbc[row]

                elif char == "{":
                    output = output + font.char_crbo[row]

                elif char == "'":
                    output = output + font.char_squo[row]

                elif char == "\"":
                    output = output + font.char_dquo[row]

                elif char == "$":
                    output = output + font.char_dolr[row]

                elif char == "/":
                    output = output + font.char_fsls[row]

                elif char == "\\":
                    output = output + font.char_bsls[row]

                elif char == "&":
                    output = output + font.char_ands[row]

                elif char == "|":
                    output = output + font.char_verb[row]
                    
                else:
                    print "Invalid character! ", char, " is not valid!"

                char_number = char_number + 1

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
    ft = fancy_title("BRi\NHIyz\NHuba\N x8\NLinux\Nh%o", ff)
    pt = plain_title("Hi")
    ft.print_art()
    pt.print_art()

