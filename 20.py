import numpy as np #объединение/разделение массивов
a = np.fromstring('1 2 3 4',sep=' ',dtype='int8')
b = np.fromstring('5 6 7 8',sep=' ',dtype='int8')
print(a)
print(b)

c= np.column_stack([a,b])#obiedinenie 2h massivov v matrizu po stolbcam
print(c)

d= np.row_stack([a,b])#po strokam
print(d)