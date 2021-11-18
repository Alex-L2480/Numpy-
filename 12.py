import numpy as np#изменение формы массивов и добавление осей
a = np.arange(32).reshape(8,2,2)
print(a)
b = np.expand_dims(a,axis=0)#dobavl osi v nachalo
print(b)
print(a.shape)
print(b.shape)