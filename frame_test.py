from py_ascii_art import framed_text

lis = ["Hello, World!&N",
       "&THow are we today? It's a nice day isn't it?"]

framed = framed_text(lis,
                     filler = "#",
                     frame_width = 1,
                     side_fr = True,
                     holder = " ",
                     width = 32)
framed.print_art()
