def drawStars(lst):
    i = 0
    while i < len(lst):
        if type(lst[i]) == str:
            i += 1
            continue
        if i + 1 < len(lst) and type(lst[i+1]) == str:
            char = lst[i+1].lower()[0]
        else:
            char = "*"
        j = 0
        string = ""
        while j < lst[i]:
            string += char
            j += 1
        print string
        i += 1

drawStars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])