#!/usr/bin/env python
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

import py_ascii_art.titles

def test():
    title_as = py_ascii_art.titles.ascii_art_str("ascii")
    title_as.print_art()
    print "\n"
    print """Type a word to generate ascii art
or type quit to stop the program.
Quit is NOT case sensitive!""" 

    usr_in = raw_input("Type something: ")
    print "\n"
    while usr_in.upper() != "QUIT":
       txt_as = py_ascii_art.titles.ascii_art_str(usr_in)
       txt_as.print_art()
       usr_in = raw_input("Type something: ")
       print "\n"

    print "\n"
    title_as.change_text("Bye now")
    title_as.print_art()
    raw_input("\nPress enter to continue...")

test()
