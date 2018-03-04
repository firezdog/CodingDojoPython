#Print all odd numbers from 1 to 1000
i = 1
while i < 1000:
    print i
    i += 2

#Print multiples of 5 from 5 to 1,000,000
i = 5
while i < 1000000:
    print i
    i += 5

#Print sum of the list and average of the list
a = [1, 2, 5, 10, 255, 3]
sum = 0
for item in a:
    sum += item
average = sum / len(a)
print "Sum:",sum,"Average:",average