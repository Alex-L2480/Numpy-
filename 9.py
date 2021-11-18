import numpy as np##изменение формы массивов и добавление осей
a = np.arange(10)
print(a)
a.shape = -1,2
b=a.view()
print(b)
a.shape = 10
print(a)
print(b)
a.shape = -1,5
print(a)
a.shape = -1
print(a)