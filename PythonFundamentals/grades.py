import random

def grades():
    i = 0
    while i < 10:
        score = int(random.random() * 101)
        if (score < 60):
            grade = "F"
        elif (score < 70):
            grade = "D"
        elif (score < 80):
            grade = "C"
        elif (score < 90):
            grade = "B"
        else:
            grade = "A"
        print("Your score is " + str(score) + ";"" your grade is " + grade + ".")
        i += 1