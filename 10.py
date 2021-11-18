import numpy as np #изменение формы массивов и добавление осей
a = np.arange(10)
print(a)
a.shape=1,-1
print(a)
b = a.T# srok-==stolbci
print(b)
a.resize(2,5)#izmen razmerov
print(a)
