#Assignment: write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

while True:
    strings = input("Enter a list of strings: ")
    character = raw_input("Enter a character to search for: ")
    results = list()
    for string in strings:
        if string.find(character) > -1:
            results.append(string)
    print results