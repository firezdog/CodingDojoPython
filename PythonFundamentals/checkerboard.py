#Assignment: produce a "checkerboard pattern" in the console using a while loop.
string = ""
i = 0
while i < 8:
    if i%2 == 0:
        j = 0
        while j < 8:
            string += "* "
            j += 1
        print string
        string = ""
    else:
        j = 0
        while j < 8:
            string += " *"
            j += 1
        print string
        string = ""
    i += 1