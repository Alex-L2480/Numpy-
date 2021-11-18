import numpy as np # линейная алгебра
a = np.array([(1,2,3),(1,4,9),(1,8,27)])
print(a)
y = np.array([10,20,30])
invA = np.linalg.inv(a)#obratnaya matriza a
print(invA)
print(invA @ y)#vychislyaem korni uravnenia umnozh obrat matrizy na y(konechnye znach uravneniy)

