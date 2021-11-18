import numpy as np#изменение формы массивов и добавление осей
a = np.arange(10)
print(a)
a.shape = 1,-1
print(a)
b = np.squeeze(a)#udalenie pustyh osey is massiva a
print(b.shape)
print(b)