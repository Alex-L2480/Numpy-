import numpy as np #объединение/разделение массивов
a =np.arange(12)
a.resize(2,6)
print(a)

b = np.hsplit(a,2)#delenie matrizy
print(b)

c = np.vsplit(a,2)
print(c)

print(c[1])