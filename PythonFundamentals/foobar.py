#Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.
'''
For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. If it is a prime number, print "Foo". If it is a perfect square, print "Bar". If it is neither, print "FooBar". Do not use the python math library for this exercise. For example, if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".

'''

i = 100
while i <= 100000:
    j = 10
    #check to see if i is a perfect square
    while j*j <= i:
        if j*j == i:
            print i, "Bar"
            i += 1
            break
        j += 1
    #if not, check to see if i is prime
    else:
        j = 2
        foo = False
        while j < i/2:
            if i%j == 0:
                #if it is not prime...
                print i, "Foobar"
                foo = True
                i += 1
                break
            else:
                j += 1
        if not foo:
            #otherwise it's prime...
            print i, "Foo"
            i += 1