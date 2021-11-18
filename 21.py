import numpy as np #объединение/разделение массивов
a = np.arange(18)
b = np.arange(18,36)
a.resize(3,3,2)
b.resize(3,3,2)
print(a)
print(b)
print(b.shape)
print(b.size)

c = np.concatenate([a,b],axis=0)#obiedinenie 3h mernih massivov po opred osi
print(c)
print(c.shape)

d = np.concatenate([a,b],axis=1)
print(d)
print(d.shape)
print(d.size)