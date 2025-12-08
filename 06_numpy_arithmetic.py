import numpy as np

# Scalar arithmetic
# Scalar is a linear algebra term (it just means a single value)

array = np.array([1, 2, 3])
print(array + 1)
# [2 3 4]
print(array - 2)
# [-1  0  1]
print(array * 3)
# [3 6 9]
print(array / 4)
# [0.25 0.5  0.75]
print(array ** 5)
# [  1  32 243]


# Vectorized math function
# Vector is another linear algebra term
# vector is a single dimension (Such as 1-D list)
# using vectorized math function we can apply a function to an entire array without using the loop

array = np.array([1.01, 2.5, 3.99])
print(np.sqrt(array))
# [1.00498756 1.58113883 1.99749844]
print(np.round(array))
# [1. 2. 4.]
print(np.floor(array))
# [1. 2. 3.]
print(np.ceil(array))
# [2. 3. 4.]


print(np.pi)
# 3.141592653589793

# EXERCISE (circle area)
radius = np.array([1, 2, 3])
print(np.pi * radius ** 2)
# [ 3.14159265 12.56637061 28.27433388]


# Element-wise arithmetic
# each operation will be element by element between two arrays

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print(array1 + array2)
# [5 7 9]
print(array1 - array2)
# [-3 -3 -3]
print(array1 * array2)
# [ 4 10 18]
print(array1 / array2)
# [0.25 0.4  0.5 ]
print(array1 ** array2)
# [  1  32 729]


# Comparison Operators

scores = np.array([91 ,55 ,100 ,73, 82, 64])
print(scores == 100)
# [False False  True False False False]
print(scores >= 60)
# [ True False  True  True  True  True]
scores[scores < 60] = 0
print(scores)
# [ 91   0 100  73  82  64]