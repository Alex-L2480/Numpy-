import numpy as np# основные данные и создание массива
a = np.array([1,2,3,4,8])#создание массива
d=a
print(d)
print(a.dtype)# tip dannih
a[2] ='123'# izmenenie elementa
print(d)
print(a[2])
b=a[[1,1,3]]#massiv is elementov po nomeram drugogo
print(b)
print(a)
print(a.dtype)
k=a[2]+1#izmenenie elementa i zapis v peremennuyu
c = a[[True,True,False,True,False]]#bulevie znachenia - kotorie true-zapishutsa
print(c)
d=d[[0,1,2,3]]# izmenenie massiva
d = d.reshape(2,2)# izmenenie formy
print(d)
print(k)