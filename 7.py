import numpy as np
"""
Write a NumPy program to create a 4x4 array with random values, now create a new array from the said array swapping first and last rows.
"""

arr = np.random.rand(4,4)
print(arr)

arr[[0, arr.shape[1]-1]] = arr[[arr.shape[1]-1, 0]]
print(arr)
