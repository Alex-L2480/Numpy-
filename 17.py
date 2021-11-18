import numpy as np #объединение/разделение массивов
a= np.array([(1,2),(3,4)])
b= np.array([(5,6),(7,8)])
print(a)
print('massiv b',b)

c = np.hstack([a,b])#obiedin po gorizontali
print(c)
d = np.vstack([a,b,a])#obiedin po verticali
print(d)