import numpy as np

"""
    The program create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0
"""
x = np.ones((10,10))
x[1:-1,1:-1] = 0    #imply 0 to second row and col to the last(not included)
print(x)