import numpy as np #объединение/разделение массивов
a = np.arange(18)
a.resize(3,3,2)
print(a)
print(a.shape)

b = np.array_split(a,2,axis=2)#delenie na 2 po osi 2
print(b)
print(b[0].shape)