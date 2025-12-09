import numpy as np

rng = np.random.default_rng()   # rng -> Random Number Generator

print(rng.integers(1, 7))
# Random number will be generated of integer data type between 1 and 6

# For readability we can also use keyword arguments
print(rng.integers(low=1, high=7, size=3))  # we can also set the amount of numbers we need
# [4 3 5]
print(rng.integers(low=1, high=7, size=(3,2)))
# [[4 4]
#  [6 2]
#  [5 6]]


# When you’re working with NumPy’s random number generator,
# the seed acts like a “starting point” for the sequence of random numbers.
# It ensures that the random numbers you get can be reproduced every time you run the code.
rng = np.random.default_rng(seed=1)
print(rng.integers(1, 7))
# 3  (1st print)
# 3  (2nd print)
# 3  (3rd print)
# 3  (4th print)


# Floating Point Numbers
print(np.random.uniform())    # uniform means uniform distribution (each value has an equal chance of being selected)
# 0.5636024165696689
print(np.random.uniform(low=-1, high=1, size=3))
# [ 0.28828398  0.21163218 -0.49596851]
np.random.seed(seed=1)   # To set the seed
print(np.random.uniform(low=-1, high=1))
# -0.165955990594852



# How to shuffle an array
array = np.array([1, 2, 3, 4, 5])
print(array)
# [1 2 3 4 5]
rng.shuffle(array)
print(array)
# [5 1 2 3 4]

# .choice() method is used to get a random choice from array
fruits = ["apple", "orange", "banana", "coconut", "pineapple"]
fruit = rng.choice(fruits)
print(fruit)
# pineapple
fruits = rng.choice(fruits, size=3)
print(fruits)
# ['pineapple' 'orange' 'orange']