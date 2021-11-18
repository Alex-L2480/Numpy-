import numpy as np
from numpy.lib.function_base import copy #индексация срезы итерирование массивов
a = np.arange(1,82)
a.resize(3,3,3,3)#zadanie 4h mernogo massiva
print(a)
print(a.shape)
b = a[:,1,:,:]#srez - ubiraem elementy osi 1 delaem 3h merny massiv
print(b)
print(b.shape)
print(b.size)
print(a.size)

c=copy(b)
c[0]=[0]
print(a[0])# pri izmen elementa predstavlenia menyaetsa i ishodny massiv
# poetomu ispolz kopia - c