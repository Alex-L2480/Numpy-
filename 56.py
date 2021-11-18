import numpy as np # математические функции
a = np.array([1,2,3,4])
a.resize(2,2)#preobrazovanie v dvumerniy massiv
print(a)
b = a.sum(axis = 0)#summa po stolbcam
c = a.sum(axis = 1)#summa po strokam
d = a.max(axis = 1)#max po strokam
print(b)
print(c)
print(d)
