import numpy as np# функции автозаполнения
a=np.empty((3,2),dtype='int8')#proizvol chisla tipa int8
print(a)
b=np.eye(4)#matriza 4 na 4 diagon is 1
print(b)
c=np.diag([1,8,3])#diagon massiva sost is chisel
print(c)
d= np.full((3,4),5)#polnostiu zapolnen 5 
print(d)