import numpy as np # произведение матриц и векторов
a = np.arange(1,4)
b = np.arange(1,7)
b = b.reshape(3,2)
print(a)
print(b)
c = np.dot(a,b)#umnozh vektora na matrizu
print(c)#stroka umnozh na 1 stolbec -1e chislo potom 2stroka umnozh na 2i stolbec -2e chislo
a = np.array([1,2])# a - vektor iz 2 znaceniy
d = np.dot(b,a)
print(np.dot(b,a))#poluchim vektor iz 3h znaceniy (3stoki v b)
a.shape = -1,1#izmenenie formy dlya poluch pri umnozhenii stolbca a ne stroki
print(a)
print(b@a)
print(b)