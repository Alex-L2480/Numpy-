import numpy as np #индексация срезы итерирование массивов
a = np.arange(1,13).reshape(3,4)
print(a)
i = [2,1,0]#nomera strok menyaem
b = a[i]
print(b)

y = np.array([[1,0],[2,1]])#kak upakovat stoki massiva a v novyi - c
c = a[y]
print(c)
