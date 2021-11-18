import numpy as np # множества unique и опрерации над ними
a = np.array([1,2,3,4,4,3,2,1])
b = np.unique(a)#massiv is unikalnyh znacheniy massiva a
print(b)
c = np.unique(a,return_counts=True)#kolich povtoreniy
print(c)
d = np.unique(a,return_index=True)#indexy pervyh vhozhdeniy
print(d)
e = np.unique(a,return_inverse=True)#massiv iz indexov unikal znacheniy
print(e)
print(e[0])#sam massiv unik
print(e[1])#indexy
print(e[0][e[1]])# vosstanovleniy massiv a