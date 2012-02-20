#ascii_art_titles.py
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


import ascii_art_font

class ascii_art_str:
    def __init__(self, text):
        self.change_text(text)

    def change_text(self, text):
        self.art = ""
        rows_content = self.parse_text(text)
        row = 0
        while row < len(rows_content):
            self.art = self.art + self.gen_ascii_art(rows_content[row])
            row = row + 1
        
    def parse_text(self, input_s):
        input_s = input_s.upper()
        chars = list(input_s)
        row_s = ""
        char_count = 0
        output = []
        first = True

        while char_count < len(chars):
            prev = char_count - 1
            nxt = char_count + 1
            if chars[char_count] == "\\" :
                if char_count < (len(chars) - 1):
                    if chars[nxt] == "N":
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

                    else:
                        row_s = row_s + chars[char_count]

                else:
                    row_s = row_s + chars[char_count]

            else:
                row_s = row_s + chars[char_count]

            char_count = char_count + 1

        output.append(row_s)
        return output

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
                    output = output + ascii_art_font.char_A[row]

                elif char == "B":
                    output = output + ascii_art_font.char_B[row]
                    
                elif char == "C":
                    output = output + ascii_art_font.char_C[row]

                elif char == "D":
                    output = output + ascii_art_font.char_D[row]

                elif char == "E":
                    output = output + ascii_art_font.char_E[row]

                elif char == "F":
                    output = output + ascii_art_font.char_F[row]

                elif char == "G":
                    output = output + ascii_art_font.char_G[row]

                elif char == "H":
                    output = output + ascii_art_font.char_H[row]

                elif char == "I":
                    output = output + ascii_art_font.char_I[row]

                elif char == "J":
                    output = output + ascii_art_font.char_J[row]

                elif char == "K":
                    output = output + ascii_art_font.char_K[row]

                elif char == "L":
                    output = output + ascii_art_font.char_L[row]

                elif char == "M":
                    output = output + ascii_art_font.char_M[row]

                elif char == "N":
                    output = output + ascii_art_font.char_N[row]

                elif char == "O":
                    output = output + ascii_art_font.char_O[row]

                elif char == "P":
                    output = output + ascii_art_font.char_P[row]

                elif char == "Q":
                    output = output + ascii_art_font.char_Q[row]

                elif char == "R":
                    output = output + ascii_art_font.char_R[row]

                elif char == "S":
                    output = output + ascii_art_font.char_S[row]

                elif char == "T":
                    output = output + ascii_art_font.char_T[row]

                elif char == "U":
                    output = output + ascii_art_font.char_U[row]

                elif char == "V":
                    output = output + ascii_art_font.char_V[row]

                elif char == "W":
                    output = output + ascii_art_font.char_W[row]

                elif char == "X":
                    output = output + ascii_art_font.char_X[row]

                elif char == "Y":
                    output = output + ascii_art_font.char_Y[row]

                elif char == "Z":
                    output = output + ascii_art_font.char_Z[row]

                elif char == " ":
                    output = output + ascii_art_font.char_space[row]

                elif char == "0":
                    output = output + ascii_art_font.char_0[row]

                elif char == "1":
                    output = output + ascii_art_font.char_1[row]

                elif char == "2":
                    output = output + ascii_art_font.char_2[row]

                elif char == "3":
                    output = output + ascii_art_font.char_3[row]

                elif char == "4":
                    output = output + ascii_art_font.char_4[row]

                elif char == "5":
                    output = output + ascii_art_font.char_5[row]

                elif char == "6":
                    output = output + ascii_art_font.char_6[row]

                elif char == "7":
                    output = output + ascii_art_font.char_7[row]

                elif char == "8":
                    output = output + ascii_art_font.char_8[row]

                elif char == "9":
                    output = output + ascii_art_font.char_9[row]

                elif char == "-":
                    output = output + ascii_art_font.char_dash[row]

                elif char == "_":
                    output = output + ascii_art_font.char_uscr[row]

                elif char == "=":
                    output = output + ascii_art_font.char_equa[row]

                elif char == "+":
                    output = output + ascii_art_font.char_plus[row]

                elif char == ".":
                    output = output + ascii_art_font.char_fstp[row]

                elif char == ",":
                    output = output + ascii_art_font.char_comm[row]

                elif char == ":":
                    output = output + ascii_art_font.char_colo[row]

                elif char == ";":
                    output = output + ascii_art_font.char_seco[row]

                elif char == "!":
                    output = output + ascii_art_font.char_excl[row]

                elif char == "?":
                    output = output + ascii_art_font.char_ques[row]

                elif char == "%":
                    output = output + ascii_art_font.char_perc[row]

                elif char == "@":
                    output = output + ascii_art_font.char_atsg[row]

                elif char == ">":
                    output = output + ascii_art_font.char_gulc[row]

                elif char == "<":
                    output = output + ascii_art_font.char_gulo[row]

                elif char == "#":
                    output = output + ascii_art_font.char_hash[row]

                elif char == "*":
                    output = output + ascii_art_font.char_star[row]

                elif char == ")":
                    output = output + ascii_art_font.char_brcc[row]

                elif char == "(":
                    output = output + ascii_art_font.char_brco[row]

                elif char == "]":
                    output = output + ascii_art_font.char_sqbc[row]

                elif char == "[":
                    output = output + ascii_art_font.char_sqbo[row]

                elif char == "}":
                    output = output + ascii_art_font.char_crbc[row]

                elif char == "{":
                    output = output + ascii_art_font.char_crbo[row]

                elif char == "'":
                    output = output + ascii_art_font.char_squo[row]

                elif char == "\"":
                    output = output + ascii_art_font.char_dquo[row]

                elif char == "$":
                    output = output + ascii_art_font.char_dolr[row]

                elif char == "/":
                    output = output + ascii_art_font.char_fsls[row]

                elif char == "\\":
                    output = output + ascii_art_font.char_bsls[row]

                elif char == "&":
                    output = output + ascii_art_font.char_ands[row]

                elif char == "|":
                    output = output + ascii_art_font.char_verb[row]
                    
                else:
                    print "Invalid character! ", char, " is not valid!"

                char_number = char_number + 1

            output = output + "\n"
            row = row + 1
            char_number = 0
            
        return output

    def print_art(self):
        print self.art
