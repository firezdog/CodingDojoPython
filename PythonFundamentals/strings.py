#1
words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day")
moreWords = words.replace("day", "month")
print moreWords

#2
x = [2,54,-2,7,12,98]
print min(x), max(x)

#3
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
xFirstHalf = x[0:len(x)/2]
xSecondHalf = x[len(x)/2:]
xSecondHalf.insert(0, xFirstHalf)
print xSecondHalf