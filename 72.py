import numpy as np # множества unique и опрерации над ними
a=np.arange(1,10)
a=a.reshape(3,3)
print(a)
b = np.unique(a)#massiv is unikalnyh znacheniy massiva a(matrizy) na vyhode - odnomer
print(b)
c = np.unique(a,axis=0)#otbor unikalnyh srok
print(c)