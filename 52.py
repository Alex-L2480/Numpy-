import numpy as np # # булевые
a = np.array([1,2,np.inf,np.nan])
b = np.isfinite(a)# true - chisla false-nan i inf
print(b)
