import numpy as np #объединение/разделение массивов
a = np.fromiter(range(18),dtype='int32')
b = np.fromiter(range(18,36),dtype='int32')#zadanie massiva iteraziey
print(a)
print(b)
a.resize(3,3,2)
b.resize(3,3,2)
print(a)
print(b)

c=np.hstack([a,b])#obiedinenie 3h mernogo massiva po osi 1
print(c)
print(c.shape)
