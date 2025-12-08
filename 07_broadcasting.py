# Broadcasting allows numpy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape

# RULES FOR BROADCASTING
# The dimensions have the same size
# OR
# One of the dimensions has the size of 1.

import numpy as np

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)
print(array2.shape)
# (1, 4)
# (4, 1)
# These arrays can be broadcast because both array's shape has column == 1 on either shape

print(array1 * array2) 
# [[ 1  2  3  4]
#  [ 2  4  6  8]
#  [ 3  6  9 12]
#  [ 4  8 12 16]]



array1 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)
print(array2.shape)
# (2, 4)
# (4, 1)
# print(array1 * array2)
# This will give an value error because on col[0] of dimensions of either array has 1 nor are they equal

