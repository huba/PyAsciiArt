def _separate_words(string):
    """this function chops up a string into words
assuming each word is separated by a space. it
puts each space as a separate word it takes one
argument the string"""
    char_list = list(str(string))
    word_list = [""]

    word_index = 0
    for char in char_list:
        #iterates over the characters list and if the character is a space it
        if str(char) == " ":
            word_index += 1
            word_list.append("")
            word_list[word_index] += str(char)
            word_index += 1
            word_list.append("")

        else:
            word_list[word_index] += str(char)

    return word_list

def wrap(width, string):
    """this function wraps the text into the
next line if the word does not fit the current
line. it take s two arguments, the line width and the string."""
    words = separate_words(string)
    rows = [""]
    
    word_count = 0
    col = 0
    while word_count < len(words):
        if len(words[word_count]) - 1 < width - col:
            rows[len(rows) - 1] += words[word_count]
            col += len(words[word_count])
            word_count += 1

        else:
            if len(words[word_count]) > width:
                for i in words[word_count]:
                    rows[len(rows) - 1] += i
                    col += 1

                    if col > width:
                        rows.append("")
                        col = 0

                word_count += 1
                
            else:
                rows.append("")
                col = 0

    chop_spaces(rows)    
    return rows

def _chop_spaces(rows):
    """this function chops of uneccessary spaces from the wrapped text"""
    for i in range(len(rows) - 1):
        charlist = list(rows[i])
        if charlist[0] == " ":
            charlist.pop(0)

        end_space = True
        for k in range(len(charlist) - 1, 0, -1):
            if charlist[k] == " ":
                if end_space:
                    charlist.pop(k)

            else:
                end_space = False

        row = ""
        for j in charlist:
            row += j

        rows[i] = row

hola = """A context manager is an object that defines the runtime context to be established when executing a with statement. The context manager handles the entry into, and the exit from, the desired runtime context for the execution of the block of code. Context managers are normally invoked using the with statement (described in section The with statement), but can also be used by directly invoking their methods."""

tsil = wrap(43, hola)
for i in tsil:
    print i
