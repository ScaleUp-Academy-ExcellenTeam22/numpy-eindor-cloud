import numpy as np
"""
8.	Write a NumPy program to replace all numbers in a given array which is equal, less and greater to a given number.
"""
num = 6
x = np.arange(10).reshape(5,2)
rows,cols = x.shape

x = np.array(x).flatten()   #make the matrix to be an array

for i in range(x.size):
    if (x[i] < 6):
        x[i] = 6

x = x.reshape(rows, cols)   #back to original shape
print(x)