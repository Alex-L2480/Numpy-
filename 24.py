import numpy as np
from numpy.lib.shape_base import hsplit, vsplit #объединение/разделение массивов
a =np.arange(10)
print(a)

b= hsplit(a,2)#RAZDELENIE STrochki NA 2
print(b)

a.shape =10,-1
print(a)

c = vsplit(a,2)#razdelenie stolbca na 2
print(c)