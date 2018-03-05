#Assignment: produce a "checkerboard pattern" in the console using a while loop.

string1 = "* * * *"
string2 = " * * * *"
i = 0
while i < 8:
    if i%2 == 0:
        print string1
    else:
        print string2
    i += 1