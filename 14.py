import numpy as np#изменение формы массивов и добавление осей
a = np.arange(10)
print(a)
a.shape = -1,1# dlya transponirovaniya dobavl os
print(a)
print(a.T)

