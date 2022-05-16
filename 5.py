import numpy as np

"""
    The program create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0
"""

x = np.ones((10,10))
y = np.array([3, 3, 3])
result = np.empty_like(x)
for i in range(10):
  result[i, :] = x[i, :] + y
print(x)