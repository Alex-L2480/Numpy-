import numpy as np # # булевые
a = np.array([1,2,3,4])
b = np.array([3,0,4,0])
c = np.logical_and(a,b)# gde est 0 - false
print(c)