# Aggregate functions = summarize data and typically
#                       returns a single value

import numpy as np

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

print(np.sum(array))   # sum of array
# 55
print(np.mean(array))  # mean of array
# 5.5
print(np.std(array))   # (standard deviation) -> measure of spread
# 2.8722813232690143
print(np.var(array))   # (variance) -> square of standard deviation
# 8.25
print(np.min(array))   # minimum value of array
# 1
print(np.max(array))   # maximum value of array
# 10
print(np.argmin(array)) # (argument minimum) -> index of minimum value
# 0
print(np.argmax(array)) # (argument maximum) -> index of maximum value
# 9

print(np.sum(array, axis=0))  # sum of columns
# [ 7  9 11 13 15]
print(np.sum(array, axis=1))  # sum of rows
# [15 40]