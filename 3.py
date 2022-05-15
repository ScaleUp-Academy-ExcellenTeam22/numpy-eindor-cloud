import numpy as np

"""
    The program print the number of rows and cols in the matrix
"""
arr = np.arange(15, dtype=np.int64).reshape(3, 5)
print(arr)

print(arr.shape)