#python learning_numpy.py
import numpy as np

# e_list = [[45, 55, 65, 78, 88],
# 			[5, 75, 46, 53, 11],
# 			[4, 5, 6, 7, 8]]
# e_array = np.array(e_list)
# print(e_array)
#=====================================
# print(np.zeros(10))
# print(np.ones(50))
#=====================================
array_1 = np.array([1, 2, 3])

print(array_1[0])
print(array_1[1:3])
mask = (array_1 % 3 == 0)
print(array_1[mask])