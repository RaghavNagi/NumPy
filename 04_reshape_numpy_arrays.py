# reshape() = Changes the shape of a array
#             w/o altering it's underlying data
#             .reshape(rows, columns)

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(array.shape)
# (12,)

# reshape function returns an array so we can reassign it
array = array.reshape(2, 6)
# during reshape elements of number should be same
# array.reshape(3, 6)  -> ValueError
# array.reshape(1, 6)  -> ValueError
print(array)
# [[ 1  2  3  4  5  6]
#  [ 7  8  9 10 11 12]]
print(array.shape)
# (2, 6)


# We can also change the dimension of array
array = array.reshape(2, 2, 3)
print(array)
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]

print(array.shape)
# (2, 2, 3)


# if we set one of the dimensions to (-1) numpy will handle the rest and adjust accordingly to other given dimensions
array = array.reshape(-1, 1)
print(array.shape)
# (12, 1)

array = array.reshape(1, -1)
print(array.shape)
# (1, 12)