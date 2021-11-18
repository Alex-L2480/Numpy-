import numpy as np # произведение матриц и векторов
a = np.arange(1,10)
print(a)
b = np.ones(9)
print(b)
c = np.inner(a,b)#umnozhenie vektorov vnutrennee - chislo
print(c)
d = np.outer(a,b)#vneshnee umnozhenie - matriza
print(d)
print(a@b)# analog dot