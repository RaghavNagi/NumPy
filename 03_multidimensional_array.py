import numpy as np

array = np.array('A')
print(array.ndim)  # ndim -> number of dimensions
print(array.shape)
# 0
# ()

print()


array = np.array(['A', 'B', 'C', 'D', 'E'])
print(array.ndim)  
print(array.shape)
# 1
# (5,)

print()


array = np.array([['A', 'B', 'C'],
                  ['D', 'E', 'F'],
                  ['G', 'H', 'I']])
print(array.ndim) 
print(array.shape)
# 2
# (3, 3)

print()


array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])
# Each 1-D list needs a consistent number of elements with each other
## their length should be same
# Otherwise it shows ValueError
print(array.ndim)
print(array.shape)
# 3
# (3, 3, 3)
# (depth, no._of_rows, no._of_columns)


print()


array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],])
print(array.ndim)
print(array.shape)
# 3
# (2, 3, 3)

print(array[0][0][0])   # chain indexing 
# 'A'

# Multidimensional Indexing is faster than chain indexing
print(array[0, 0, 0]) # multidimensional indexing
# 'A' 