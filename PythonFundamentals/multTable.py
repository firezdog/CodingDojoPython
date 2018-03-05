print "x",1,2,3,4,5,6,7,8,9,10,11,12
i = 0
while i < 12:
    j = 0
    string = str(i+1)
    while j < 12:
        string += " " + str((i+1)*(j+1))
        j += 1
    print string
    string = ""
    i += 1