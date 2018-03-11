def number1():
    for i in range(1,256):
        print(i)

def number2():
    for i in range(1,256,2):
        print(i)

def number3():
    sum = 0
    for i in range(0,256):
        sum += i
        print(i, sum)

def number4(myList):
    for item in myList:
        print(item)

def number5(myList):
    max = myList[0]
    for item in myList:
        if max < item:
            max = item
    return max

def number6(myList):
    sum = 0.0
    for item in myList:
        sum += item
    return float(sum / len(myList))

def number7():
    myList = []
    for i in range(1,256,2):
        myList.append(i)
    return myList

def number8(myLst):
    i = 0
    while i<len(myLst):
        myLst[i] *= myLst[i]
        i += 1
    return myLst

def number9(myLst, y):
    count = 0
    for item in myLst:
        if item > y:
            count += 1
    return count

def number10(myLst):
    i = 0
    while i < len(myLst):
        if myLst[i] < 0:
            myLst[i] = 0
        i += 1
    return myLst

def number11(myLst):
    print "Max: ", number5(myLst)
    print "Average: ", number6(myLst)
    min = myLst[0]
    for item in myLst:
        if item < min:
            min = item
    print "Min: ", min

def number12(myLst):
    i = 0
    while i < len(myLst)-1:
        myLst[i] = myLst[i+1]
        i+=1
    myLst[len(myLst)-1] = 0
    return myLst

def number13(myLst):
    i = 0
    while i < len(myLst):
        if myLst[i] < 0:
            myLst[i] = "Dojo"
        i += 1
    return myLst


print(number13([1,-2,3,-4]))