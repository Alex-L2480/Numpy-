import numpy as np# основные данные и создание массива
a = np.array([1,2,3,4,8],'uintc')
print(a)
print(a.dtype)
y= np.int16(10.5)#tip 16 - na vyhode prosto 10
print(y)
a[2]=a[2]+1# izmen elementa
print(a)
t=np.complex64(a)#izmen tipa dannyh

print(t)
print(t.dtype)
