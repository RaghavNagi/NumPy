import numpy as np

# .zeros function will return the array of zeros
# we just have to pass the dimensions
array = np.zeros(10)
print(array)
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
array = np.zeros((2, 10))
print(array)
# [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
array = np.zeros((2, 3, 10))
print(array)
# [[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]

#  [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]]


# .ones same as zeros just return array of 1
array = np.ones((2, 3, 10))
print(array)
# [[[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#   [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#   [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]

#  [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#   [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#   [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]]


# .full we have to give value to fill in that array
array = np.full((2, 3, 10), 5)
print(array)
# [[[5 5 5 5 5 5 5 5 5 5]
#   [5 5 5 5 5 5 5 5 5 5]
#   [5 5 5 5 5 5 5 5 5 5]]

#  [[5 5 5 5 5 5 5 5 5 5]
#   [5 5 5 5 5 5 5 5 5 5]
#   [5 5 5 5 5 5 5 5 5 5]]]


# .eye this function makes an identity array made with 0 and 1
array = np.eye(2)
print(array)
# [[1. 0.]
#  [0. 1.]]


# .empty this function makes an empty array we just have to pass the dimensions
# array will be filled with garbage value
# .empty function is faster than .zeros function
array = np.empty((2, 3))
print(array)
# [[0. 0. 0.]
#  [0. 0. 0.]]


# .arange (start, stop, step)
array = np.arange(0, 10)
print(array)
# [0 1 2 3 4 5 6 7 8 9]
array = np.arange(0, 100, 2)
print(array)
# [ 0  2  4  6  8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46
#  48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94
#  96 98]
array = np.arange(0, 10, .1)
print(array)
# [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7
#  1.8 1.9 2.  2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3.  3.1 3.2 3.3 3.4 3.5
#  3.6 3.7 3.8 3.9 4.  4.1 4.2 4.3 4.4 4.5 4.6 4.7 4.8 4.9 5.  5.1 5.2 5.3
#  5.4 5.5 5.6 5.7 5.8 5.9 6.  6.1 6.2 6.3 6.4 6.5 6.6 6.7 6.8 6.9 7.  7.1
#  7.2 7.3 7.4 7.5 7.6 7.7 7.8 7.9 8.  8.1 8.2 8.3 8.4 8.5 8.6 8.7 8.8 8.9
#  9.  9.1 9.2 9.3 9.4 9.5 9.6 9.7 9.8 9.9]


# .linspace (means -> linear space)
# (start, stop, num)
# it works just as arrange function
# the thing that makes it different from arrange is that we're defining the number of points that we want (that is the num argument)
# the spacing between the each is going to be calculated for us
array = np.linspace(0, 10, 3)
print(array)
# [ 0.  5. 10.]
array = np.linspace(0, 10, 4)
print(array)
# [ 0.          3.33333333  6.66666667 10.        ]