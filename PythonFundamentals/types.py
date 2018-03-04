while True:
    entry = input("Enter a value (strings in quotes): ")
    etype = type(entry)        
    if entry == "q":
        exit()
    else:
        if etype == int:
            if entry > 100:
                print("That's a big number!")
            else:
                print("That's a small number...")

        if etype == str:
            if len(entry) > 50:
                print("That's a long sentence!")
            else:
                print("That's a short sentence...")

        if etype == list:
            if len(entry) > 10:
                print("That's a long list!")
            else:
                print("That's a short list...")