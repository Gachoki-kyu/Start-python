import numpy as np
from numpy import random
'''
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
'''


# 2-D 
arafu = np.array([[1,2,3],[4,5,6]])
print(arafu)
'''
print(arafu.ndim)
print("second element in first row", arafu[0,1])
for x in arafu:
   # print(x)
    for y in x:
        print(y)
'''
x = random.randint(50, size=(3,5))
print(x)


