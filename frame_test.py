import py_ascii_art.text_frame

framed = py_ascii_art.text_frame.framed_text("\THey Hello\NHuba",
                                             filler = "*",
                                             frame_width = 2,
                                             side_fr = True,
                                             holder = " ")
framed.print_art()
