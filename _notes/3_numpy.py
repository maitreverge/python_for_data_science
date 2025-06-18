import numpy as np

L1 = [1, 2, 3, 4,]
L2 = [5, 6 , 7, 8]
L3 = [9, 10, 11, 12]

# Need to init in a lsit the collection of the several lists
a = np.array([L1, L2, L3])

print(a)

# Access the numpy array precise index with [row, column]
print(a[2, 2])

print(f"a.ndim = {a.ndim}")
print(f"a.shape = {a.shape} : (rows, columns)")

print(f"a.size = {a.size} : number of total elements")

print(f"a.dtype = {a.dtype} : What is the type of the data, which is generally homogenous")

