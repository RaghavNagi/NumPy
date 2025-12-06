# dtype = Keyword Arguments that tells NumPy what kind of values are stored in an array
#         Otherwise NumPy guesses the best data type based on your data
#         Manually setting dtype improves performance
#         & is more memory efficient (especially when working with large data sets)

# integer (int8, int16, int32, int64)
# float (float16, float32, float64)
# boolean (bool_)
# string (str_, <U#)
# object (object_)

import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)
print(array.dtype)
print(f"{array.nbytes} bytes")
# [1 2 3 4 5]
# int64
# 40 bytes

print()

array1 = np.array([1, 2, 3, 4, 5], dtype=np.int32)
print(array1)
print(array1.dtype)
print(f"{array1.nbytes} bytes")
# [1 2 3 4 5]
# int32
# 20 bytes

print()

array2 = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(array2)
print(array2.dtype)
print(f"{array2.nbytes} bytes")
# [1. 2. 3. 4. 5.]
# float64
# 40 bytes

print()

array3 = np.array([1, 2, 3, 4, 5, 0], dtype=np.bool_)
# bool -> it is a python boolean
# bool_ -> it is a numpy boolean
print(array3)
# 0 -> False
# !0 -> True
print(array3.dtype)
print(f"{array3.nbytes} bytes")
# [ True  True  True  True  True False]
# bool
# 6 bytes

print()

array4 = np.array([1, 2, 3, 4, 5], dtype=np.str_)
print(array4)
print(array4.dtype)
print(f"{array4.nbytes} bytes")
# ['1' '2' '3' '4' '5']
# <U1
# <U1 -> 1 depends on largest length of string in numpy array
# 20 bytes

array5 = np.array(["apple", "banana", "orange"], dtype=np.str_)
print(array5)
print(array5.dtype)
print(f"{array5.nbytes} bytes")
# ['apple' 'banana' 'orange']
# <U6
# 72 bytes


# we can also set the fixed length of the string
array6 = np.array(["apple", "banana", "orange"], dtype="<U4")
# now any characters beyond 4 gets truncated
print(array6)
print(array6.dtype)
print(f"{array6.nbytes} bytes")
# ['appl' 'bana' 'oran']
# <U4
# 48 bytes

print()

array7 = np.array([1, 2.1, "apple", 4, True], dtype=np.object_)
# operations fall back to python not numpy's optimized c code.
# we lose those speed advantages when working with python objects
# This allows you to mix and match data types
print(array7)
print(array7.dtype)
print(f"{array7.nbytes} bytes")
# [1 2.1 'apple' 4 True]
# object
# 40 bytes


print()


# If want to change from one data type to another after creating the array
array8 = np.array([1, 2, 3, 4, 5])

array8 = array8.astype(np.float16)

print(array8)
print(array8.dtype)
print(f"{array8.nbytes} bytes")
# [1. 2. 3. 4. 5.]
# float16
# 10 bytes

array9 = np.array([1.1, 2.2, 3.3, 4.4, 5.5])

array9 = array9.astype(np.int16)

print(array9)
print(array9.dtype)
print(f"{array9.nbytes} bytes")
# [1 2 3 4 5]
# int16
# 10 bytes