import numpy as np

array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15 ,16]
])

# array[start : end: step]


# Row Slicing

print(array[0:3])
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# Col slicing
print(array[:, 0])
# [ 1  5  9 13]
print(array[:, 0:3])
# [[ 1  2  3]
#  [ 5  6  7]
#  [ 9 10 11]
#  [13 14 15]]