PyAsciiArt
==========

* Author: Huba Z. Nagy 
* Website: https://sites.google.com/site/0x2b0xd4/
* Copyright(c) 2012 Huba Z. Nagy
* Released under the MIT Licence

PyAsciiArt is a Ascii art generator written in Python, for now it can only 
generate ascii art text in one style. It is part of my schoolwork. Run test.py
to see what the package is capable of...

Output of test.py
-----------------
	
	....###.....######...######..####.####
	...##.##...##....##.##....##..##...##.
	..##...##..##.......##........##...##.
	.##.....##..######..##........##...##.
	.#########.......##.##........##...##.
	.##.....##.##....##.##....##..##...##.
	.##.....##..######...######..####.####
	......................................



	Type a word to generate ascii art
	or type quit to stop the program.
	Quit is NOT case sensitive!
	Type something: hello\nworld


	.##.....##.########.##.......##........######.
	.##.....##.##.......##.......##.......##....##
	.##.....##.##.......##.......##.......##....##
	.#########.######...##.......##.......##....##
	.##.....##.##.......##.......##.......##....##
	.##.....##.##.......##.......##.......##....##
	.##.....##.########.########.########..######.
	..............................................
	.##......##..######..########..##.......#######.
	.##..##..##.##....##.##.....##.##.......##....##
	.##..##..##.##....##.##.....##.##.......##....##
	.##..##..##.##....##.########..##.......##....##
	.##..##..##.##....##.##...##...##.......##....##
	.##..##..##.##....##.##....##..##.......##....##
	..###..###...######..##.....##.########.#######.
	................................................

	Type something: quit




	.########..##....##.########....##....##..######..##......##
	.##.....##..##..##..##..........###...##.##....##.##..##..##
	.##.....##...####...##..........####..##.##....##.##..##..##
	.########.....##....######......##.##.##.##....##.##..##..##
	.##.....##....##....##..........##..####.##....##.##..##..##
	.##.....##....##....##..........##...###.##....##.##..##..##
	.########.....##....########....##....##..######...###..###.
	............................................................


	Press enter to continue...
	
To implement it
---------------

	```python
	import py_ascii_art

	title = py_ascii_art.titles.ascii_art_str("Hello\NWorld")
	title.print_art()
	```

This will produce:

	.##.....##.########.##.......##........######.
	.##.....##.##.......##.......##.......##....##
	.##.....##.##.......##.......##.......##....##
	.#########.######...##.......##.......##....##
	.##.....##.##.......##.......##.......##....##
	.##.....##.##.......##.......##.......##....##
	.##.....##.########.########.########..######.
	..............................................
	.##......##..######..########..##.......#######.
	.##..##..##.##....##.##.....##.##.......##....##
	.##..##..##.##....##.##.....##.##.......##....##
	.##..##..##.##....##.########..##.......##....##
	.##..##..##.##....##.##...##...##.......##....##
	.##..##..##.##....##.##....##..##.......##....##
	..###..###...######..##.....##.########.#######.
	................................................



License
-------

Copyright (c) 2012 Huba Z. Nagy <https://sites.google.com/site/0x2b0xd4/>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.