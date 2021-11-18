import numpy as np#изменение формы массивов и добавление осей
a = np.arange(32).reshape(8,2,2)
print(a)
print(a.shape)
b=np.expand_dims(a,axis=2)#dobavl osi 2
print(b)
print(b.shape)
c = np.append(b,b,axis=0)# dobavl elementa(massiv b) na os 0
print(c)
print(c.shape)