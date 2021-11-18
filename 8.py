import numpy as np #свойства и представления массивов
b = np.ones((3,4,5))#massiv is 1
j=b.view()#kopia predstavlenia massiva
u= b.copy()#kopia massiva
print(b)
print(b.ndim)#kol-vo osey
b.shape = 12,5#izmen formy predstavlenia
print(b)
b[0,0] = 666
c= b.reshape(3,2,10)
print(c)
d = c.T#peremena stolbcov so srokami v matrize
print(d)
print(j)
print(u)