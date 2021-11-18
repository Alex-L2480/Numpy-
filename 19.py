import numpy as np #объединение/разделение массивов
a = np.fromstring('1 2 3 4',sep=' ',dtype='int8')
b = np.fromstring('5 6 7 8',sep=' ',dtype='int8')
print(a)
print(b)

c=np.hstack([a,b])
print(c)
print(c.shape)

d=np.vstack([a,b])
print(d)
print(d.shape)
