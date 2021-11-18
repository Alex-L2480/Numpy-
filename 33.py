import numpy as np #индексация срезы итерирование массивов
a = np.array([(1,2,3),(4,5,6),(7,8,9)])# zadanie matrizi
print(a) 
for x in a.flat:# perebor mnogomer massiva v stroku
    print(x, end=' ')