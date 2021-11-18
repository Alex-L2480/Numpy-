import numpy as np# функции автозаполнения
a=np.tri(5)#nixhe diagonali iz 1 - tozhe 1
print(a)
b=np.tril([1,2,5,4])#zapoln po stolbcam nizhe glav diag(triu-naoborot)
print(b)
