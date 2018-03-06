def makeDict(list1,list2):
    if len(list1) > len(list2):
        return dict(zip(list1, list2)) 
    elif len(list2) > len(list1):
        return dict(zip(list2, list1))
    else:
        return dict(zip(list1,list2))

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "aardvark"]

print(makeDict(name, favorite_animal))