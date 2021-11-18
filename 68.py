import numpy as np # линейная алгебра
b = np.arange(10,19)
b = b.reshape(3,3)
print(np.linalg.matrix_rank(b))#rang mtrizy
print(b)

