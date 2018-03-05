def about(aboutMe):
    for item in aboutMe:
        string = "My "
        string += item
        string += " is "
        string += str(aboutMe[item])
        string += "."
        print(string)

about({"name": "Alex", "age": 34, "country of birth": "USA", "favorite language": "Chinese"})