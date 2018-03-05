import random
heads = 0
tails = 0
i = 0
while i < 5000:
    toss = round(random.random())
    string = "You tossed a "
    if toss == 0:
        tails += 1
        string += "tails. " 
    else:
        heads += 1
        string += "heads. "
    string += str(heads) + " head(s) and " + str(tails) + " tail(s) so far."
    print(string)
    i += 1