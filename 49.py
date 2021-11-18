import numpy as np # # булевые
a = np.array([1,2,3])
b = a[a>1]
print(b)
print(a>2)# vivod bulevyh znacheniy massiva a kot >2
print(a!=1)#vse true krome 1go elementa
print(np.any(a==1))#esli hotya by 1 element ==1 to True esli net - False
print(np.all(a>1))# esli vse elementy >1 to true