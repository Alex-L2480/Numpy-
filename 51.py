import numpy as np # # булевые
a = np.array([1,2,np.inf,np.nan])#inf - infinity
print(a)
b = np.isnan(a)# esli est nan v massive to on budet true
print(b)
f = np.isnan(a)
g = np.isinf(a)#esli est inf to true
f+=g# obiedin f i g
a = a[~f]#udalyaem inf i nan is massiva
print(a)