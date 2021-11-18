import numpy as np#изменение формы массивов и добавление осей
a = np.diag([4,2,7])#zadanie matrizi is 0 s diagon 427
print(a)
print(a[1])#vivod stroki 1
b = np.linspace(0,10,3,dtype = np.int8)#zadanie massiva ot 0 do 10 s 3 elem na ravnom rasstoyanii
print(b)
print(b[1])
c = np.fromiter('hello',dtype='U1')#zadanie massiva iz stroki iteraziey
print(c)
d = np.fromstring('1,2,3',dtype='int16',sep=',')#massiv iz stroki razdel - zapiataya
print(d)