import numpy as np # произведение матриц и векторов
a=np.arange(1,10)
b = np.arange(10,19)
a = a.reshape(3,3)
b = b.reshape(3,3)
print(a)
print(b)
c = np.dot(a,b)# matrichnoe umnozhenie sroka* stolbec potom slozhenie
print(c)
d = np.matmul(a,b)#luche ispolzovat matrichnoe umnozhenie sroka* stolbec potom slozhenie
print(d)