import numpy as np # математические функции
a = np.array([1,-2,3.5,-4])
a.resize(2,2)
print(a)
print(np.amin(a,axis=0))#minimal po stolbcam
