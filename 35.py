import numpy as np
from numpy.lib.function_base import copy #индексация срезы итерирование массивов
a = np.arange(1,82)
a.resize(3,3,3,3)#zadanie 4h mernogo massiva
print(a)
print(a.shape)
b = a[0:2,0:2,1,1]#srez - pervye 2 osi - 2 pervyh elementa
print(b)
print(b.shape)
print(b.size)
print(a.size)
print(a[0][0])
c= a[...,1,1]# v nachale polnye srezy potom elmenty nuzhnye
print(c)
