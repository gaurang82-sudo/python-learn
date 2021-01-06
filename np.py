import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6, ]])
print(array)
print(type(array))
print(array.shape)

zeros = np.zeros((3, 4), dtype=int)
print(zeros)
array = np.ones((3, 2), dtype=int)
print(array)
array = np.full((3, 4), 5, dtype=int)
print(array)
array = np.random.random((3, 4))
print(array)
print(array[0, 0])
print(array > 0.2)
print(array[array > 0.2])
print(np.round(array))
