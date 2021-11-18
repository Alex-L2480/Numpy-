import numpy as np #индексация срезы итерирование массивов
a = np.arange(1,9)
print(a)
print(a[0])
print(a[[0]])# na vyhode spisok
b=a[[0,3]]#b - noviy massiv
print(b)
i = a>3
c = a[i]#poluchaem elementy bolshe 3 novyi massiv
print(c)
c[0]=8
print(c)
print(a)
