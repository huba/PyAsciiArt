PyAsciiArt
==========

* Author: Huba Z. Nagy 
* Website: https://sites.google.com/site/0x2b0xd4/
* Copyright(c) 2012 Huba Z. Nagy
* Released under the MIT Licence

PyAsciiArt is a Ascii art generator written in Python, for now it can only 
generate ascii art text in one style. It is part of my schoolwork plus a
bit more.

Overview
--------
test.py is script demonstrates how to use all the different classes from the API.
There are classes classes

* plain_title   ascii art titles consisting of two different characters.
* fancy_title   ascii art titles using the fancy_font class.
* fancy_font   this class creates it's font style from an XML file.
* framed_text   puts text into a box.

And two other modules with methods that are only used by the classes

* text_parser   miscellanius functions used by the othr classes, like finding new line characters "&N" and tab characters "&T", &&T will return &T.
* font   contains the default values used by the plain_font class.

plain_title
-----------
```python
from py_ascii_art.titles import plain_title

pt = plain_title("Hello&NWorld")
pt.print_art()

```

fancy_title & fancy_font
------------------------
```python
from py_ascii_art.titles import plain_title, fancy_font

ffont = fancy_font("F3D_NE") #F3D_NE is the only font style
ft = fancy_title("Hello&NWorld", ffont)
ft.print_art()

```
These two classes need each other as you see the constructor
of fancy_title needs an input text and an instance of the 
fancy font class. Adding fonts is simple, there is an xml
called font_sample.xml in py_ascii_art/fonts. Fill out the
where needed, refer to the annotation.The font style is 
divided up into four zones plus one only for space,
four zones are:

* uppercase  A,  B, C ...
* lowercase  a, b, c ...
* numbers  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
* specials  +, =, ! ...

Example
-------
```xml
<font>
	<info>
		<lines>10</lines><!--The height of the characters-->
		<uppercase>false</uppercase><!--if there is an uppercase field or should the program just skip it-->
		<lowercase>false</lowercase><!--same with lowercase and so on-->
		<numbers>false</numbers>
		<specials>false</specials>
		<missing_upper><!--if you want the program to read the field but there are a few characters missing still-->
			<miss></miss><!--put the character id in here, put all of them into the appropriate field-->
		</missing_upper>
		<missing_lower>
		</missing_lower>
		<missing_num>
		</missing_num>
		<missing_spec>
		</missing_spec>
	</info>
	<space><!--field tag-->
		<char><!--character tag, one for each character in the field-->
			<char_id>char_space</char_id><!--char id don't change the contents of this tab unless you have a good reason-->
			<ln></ln><!--fill out each row of the character-->
			<ln></ln>
			<ln></ln>
			<ln></ln>
			<ln></ln>
			<ln></ln>
			<ln></ln>
			<ln></ln>
			<ln></ln>
			<ln></ln>
		</char>
	</space>
```
and so on... Than save it as whatever you want to in the py_ascii_art/fonts
folder, then open BUILTINS.xml in the py_ascii_art folder and add
a font tag like this under the root tag:
```xml
<Builtins>
	<font>
		<name>NAME</name><!--this is what you will use in the fancy_font constructor-->
		<file>fonts/whatever_you_saved_yours_as.xml</file>
	</font>
</Builtins>
```
Done.
You would use your new font as
```python
ffont = fancy_font("NAME")
```

framed_text
-----------
```python
from py_ascii_art import framed_text

lis = ["Hello, World!&N", "&THow are we today? It's a nice day isn't it?"]

framed = framed_text(lis, filler = "#", frame_width = 1, side_fr = True, holder = " ", width = 32)
framed.print_art()
```
Will produce

	################################
	#Hello, World!                 #
	#    How are we today? It's a n#
	#ice day isn't it?             #
	################################

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