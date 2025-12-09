import numpy as np

# Save a NumPy array

array = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
np.save("data", array)  # If file is not created it will automatically create a file with extension ".npy"
# we can also give path here if we want to save in any other place
# in python if we give path forward or backslashes are always doubled (//desktop)
print("NumPy array is saved")



# Load a NumPy array

array1 = np.load("data.npy")
print(array1)
# [[1 2 3]
#  [4 5 6]]



# Save multiple numpy arrays

array2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
    ])
array3 = np.array([1.1, 2.2, 3.3, 4.4])

np.savez("dataMulti", array2, array3)   # savez -> z mans zipped
# savez function save file with extension ".npz" 
# we can save multiple file with this function like 3, 4, 5 .....
print("numpy arrays are saves")

np.savez_compressed("dataMultiCompress", array2, array3)
# if we have a lot of data to work with we can save it as compressed file
# savez_compress will sve compressed file
print("compress file is saved")



# Load multiple NumPy arrays

arrays = np.load("dataMulti.npz")
print(arrays)
# NpzFile 'dataMulti.npz' with keys: arr_0, arr_1

# we can access the individual arrays with these give keys
arr1 = arrays["arr_0"]
arr2 = arrays["arr_1"]
print(arr1)
# [[1 2 3]
#  [4 5 6]]
print(arr2)
# [1.1 2.2 3.3 4.4]