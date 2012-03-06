#!/usr/bin/env python
#This file is part of the PyAsciiArt project
#Created by Huba Nagy 17.02.12
# and is released under the MIT Licence.
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

from py_ascii_art import fancy_font, plain_title, fancy_title, framed_text

TL_COMMANDS = {"QIT": ["will end the program",
                       "QUIT"],
               "PLT": ["showcases the plain titles module",
                       "PLAIN TITLES"],
               "FCT": ["showcases the new fancy titles module",
                       "FANCY TITLES"],
               "FRT": ["showcases the boxed text module",
                       "FRAMED TEXT"]}
SL_COMMANDS = {"BCK": ["goes back to top level", "BACK"]}
PROMPT = "command> "
WIDTH = 70

def test_all():
    ffont = fancy_font("F3D_NE")
    ftitle = fancy_title("PyASCII&N&TArt", ffont)
    ftitle.print_art()
    
    minstr = ["This program is showcasing the",
             " features of PyAsciiArt.&N",
             "Use one of these commands:&N"]
    for i in TL_COMMANDS:
        minstr.append("&T" + TL_COMMANDS[i][1]
                      + ": " + TL_COMMANDS[i][0] + "&N")

    minstr.append("&NYou can use the BACK command to return to this menu")

    sinstr = "Enter text, or type BACK to&Nreturn to the main menu."
        
    finstr = framed_text(minstr, width = WIDTH, filler = "#", title = "Testing", frame_title = True)
    finstr.print_art()
    
    pt = plain_title("")
    ft = fancy_title("", ffont)
    fx = framed_text("", filler = "#",
                     frame_width = 2)

    usr_in = raw_input(PROMPT)
    print ""
    while usr_in != TL_COMMANDS["QIT"][1]:
        if usr_in == TL_COMMANDS["PLT"][1]:
            finstr.change_text("Plain Titles&N" + sinstr)
            finstr.print_art()
            usr_in = raw_input(PROMPT)
            print ""
            while usr_in != SL_COMMANDS["BCK"][1]:
                pt.change_text(usr_in)
                pt.print_art()
                finstr.change_text("Plain Titles&N" + sinstr)
                finstr.print_art()
                usr_in = raw_input(PROMPT)
                print ""
                
        elif usr_in == TL_COMMANDS["FCT"][1]:
            finstr.change_text("Fancy Titles&N" + sinstr)
            finstr.print_art()
            usr_in = raw_input(PROMPT)
            print ""
            while usr_in != SL_COMMANDS["BCK"][1]:
                ft.change_text(usr_in)
                ft.print_art()
                finstr.change_text("Fancy Titles&N" + sinstr)
                finstr.print_art()
                usr_in = raw_input(PROMPT)
                print ""

        elif usr_in == TL_COMMANDS["FRT"][1]:
            finstr.change_text("Framed Text&N" + sinstr)
            finstr.print_art()
            usr_in = raw_input(PROMPT)
            print ""
            while usr_in != SL_COMMANDS["BCK"][1]:
                fx.change_text(usr_in)
                fx.print_art()
                finstr.change_text("Framed Text&N" + sinstr)
                finstr.print_art()
                usr_in = raw_input(PROMPT)
                print ""

        else:
            print "Invalid command!\n"

        finstr.change_text(minstr)
        finstr.print_art()
        usr_in = raw_input(PROMPT)

    ftitle.change_text("Quiting")
    print ""
    ftitle.print_art()
    raw_input("Press enter to continue...")
            
test_all()
