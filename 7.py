import numpy as np #свойства и представления массивов
a = np.array([1,2,3,4,8],'int64')
print(a.dtype)
print(a.itemsize)#razmer 1 elementa
a.dtype = np.int8
print(a.dtype)
print(a)
print(a.size)#kol-vo elementov
print(a.itemsize)