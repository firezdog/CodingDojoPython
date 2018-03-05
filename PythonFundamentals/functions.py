def oddEven():
    count = 1
    while count<= 2000:
        if count%2 == 0:
            kind = "even"
        else:
            kind = "odd"
        print "Number is " + str(count) + " . This is an " + kind + " numer."
        count += 1

def multiply(numbers,multiplier):
    i = 0
    while i < len(numbers):
        numbers[i] *= multiplier
        i += 1
    return numbers

def analyzeNumbers(numbers):
    analyzedNumbers = []
    i = 0
    while i < len(numbers):
        analyzedNumbers.append([])
        j = 0
        while j < numbers[i]:
            analyzedNumbers[i].append(1)
            j += 1
        i+=1
    return analyzedNumbers