import numpy as np

# b = np.array([(1,2,3,4),(1,2,3,4)])
# print(b)

# print(np.zeros((3,4)))
# print(np.ones((10,10)))

def toOnes(arr):
    newarr = []
    for number in arr:
        newarr.append(np.ones(number,dtype=np.int16))
    return newarr

print(toOnes([3,5,7]))