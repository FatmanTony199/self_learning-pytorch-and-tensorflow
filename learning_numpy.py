#python learning_numpy.py
import numpy as np

e_list = [[45, 55, 65, 78, 88],
			[5, 75, 46, 53, 11],
			[4, 5, 6, 7, 8]]
e_array = np.array(e_list)
print(e_array)

print(np.zeros(10))
print(np.ones(50))

array_1 = np.array([1, 2, 3])
print(array_1[0])
print(array_1[1:3])
mask = (array_1 % 3 == 0)
print(array_1[mask])

A = np.array([2, 4, 6])
print("A:", A)
B = np.array([4, 5, 6])
print("B:", B)
result_1 = A + B
print("A + B:", result_1)
result_2 = A - B
print("A - B:",result_2)
result_3 = A * B
print("A * B:",result_3)
result_4 = A / B
print("A / B:",result_4)

A1 = np.array([[2, 4], [6, 8]])
print("A:", A1)
B1 = np.array([[1, 3], [5, 7]])
print("B:", B)
result_1 = A1 + B1
print("A + B:", result_1)
result_2 = A1 - B1
print("A - B:",result_2)
result_3 = A1 * B1
print("A * B:",result_3)
result_4 = A1 / B1
print("A / B:",result_4)

eyes = np.eye(10)
print(eyes)

ran = np.random.rand(100)
print(ran)

ran_2D = np.random.rand(100, 50)
print(ran_2D)

randn = np.random.randn(5,5)
print(randn)

randint = np.random.randint(1,100,10)
print(randint)

randint_2D = np.random.randint(1,100,(2,3))
print(randint_2D)

arr= np.arange(25)
print(arr)
arr = arr.reshape(5,5)
print(arr)

armax = arr.max()
armin = arr.min()
print("max:", armax)
print("min:", armin)

argmax = arr.argmax()
argmin = arr.argmin()
print("argmax", argmax)
print("argmin", argmin)

x = np.array([2, 0, 6])
y = np.array([3, 5, -1])
z = np.array([1, 4, 7])
print("dot x y :", np.dot(x, y))
print("dot x z :", np.dot(x, z))

x = np.array([2, 0, 6])
y = np.array([3, 5, -1])
print("cross x y:",np.cross(x, y))
print("cross y z:",np.cross(y, x))

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
