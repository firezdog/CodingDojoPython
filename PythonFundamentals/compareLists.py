while True:
    list1 = input("\nInput first list: ")
    list2 = input("Input second list: ")
    if len(list1) != len(list2):
        print("The lists are not the same.\n")
    else:
        same = True
        i = 0
        while i < len(list1):
            if list1[i] == list2[i]:
                i += 1
                continue
            else:
                print("The lists are not the same.\n")
                same = False
                break
        if (same == True):
            print("The lists are the same\n")