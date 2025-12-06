# Numpy = Numerical Python
# numpy is written in C language that's why it makes python a little faster to use than regular python code.
# we can also perform vectorized operation using numpy arrays
#  eg :- np.array([1,2,3])*2 = [2,4,6]

import numpy as np

# print(np.__version__)
# to check numpy version

my_list = [1,2,3,4]
my_list *= 2
print(my_list)
# [1, 2, 3, 4, 1, 2, 3, 4]


array = np.array([1,2,3,4])
array *= 2
print(array)
# [2 4 6 8]