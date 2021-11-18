import numpy as np # # булевые
a = np.array([True,False,True,False])
b = np.array([True,True,False,False])
c = np.logical_and(a,b)#true - tolko tam gde oba elementa - true
print(c)
d = np.logical_or(a,b)#-esli 1 is 2h true to true
print(d)
e = np.logical_not(a)#inversia 
print(e)
