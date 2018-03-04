while True:

    entry = input("Enter a list of strings and / or numbers: ")

    if type(entry) != list:
        exit()

    concat = ""
    total = 0
    stringFound = False
    numberFound = False

    for item in entry:
        if type(item) == str:
            stringFound = True
            concat += item
        if type(item) == int or type(item) == float:
            numberFound = True
            total += item
    
    if stringFound and numberFound:
        print("The list type is mixed.")
        print(concat)
        print(total)
    elif stringFound:
        print("The list type is str")
        print(concat)
    else:
        print("The list type is int")
        print(total)