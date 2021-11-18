import numpy as np #объединение/разделение массивов
a = np.arange(8)
b = np.arange(8,16)
c= np.r_[a,b]
print(c)

d = np.c_[a,b]#obiedinenie v stolbcy
print(d)

e = np.c_[1:5]
print(e)
