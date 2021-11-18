import numpy as np#изменение формы массивов и добавление осей
a = np.arange(10)
a.shape = -1,5
print(a)
b= a.reshape(10)#izmen formi matrizi v sroku
print(b)
print(a)
