import numpy as np # множества unique и опрерации над ними
x = np.array([0,1,2,3])
y = np.arange(1,9)
print(np.intersect1d(x,y))#znachenia kotorye est v oboih massivah
print(np.union1d(x,y))#massiv is vseh unikalnyh elementov 2h massivov
print(np.setdiff1d(x,y))#vychitanie - ostanetsya tolko elementy unikal dlya massiva x
print(np.setdiff1d(y,x))
print(np.setxor1d(x,y))# tolko elementy kot ne povtoryautsa v oboih massivah