import numpy as np # линейная алгебра
a = np.array([(1,2,3),(1,4,9),(1,8,27)])
print(a)
print(np.linalg.matrix_rank(a))#rang mtrizy
y = np.array([10,20,30])# znacheniya kot dolzhny poluchitsya is 3 uravneniy 1y matrizy
print(np.linalg.solve(a,y))#reshaet uravnenie
