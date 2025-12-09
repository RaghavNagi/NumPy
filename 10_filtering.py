# Filtering = Refers to the process of selecting elements
#             from an array that match a given condition.

import numpy as np

ages = np.array([
    [21, 17, 19, 20, 16, 30, 18, 65],
    [39, 22, 15, 99, 18, 91, 20, 21]
])

teenagers = ages[ages < 18]   # This is boolean indexing
# By using boolean indexing this will flatten 2-D array
print(teenagers)
# [17 16 15]

adults = ages[(ages >= 18) & (ages < 65)]
print(adults)
# [21 19 20 30 18 39 22 18 20 21]


# .where() function is for filtering and creating the new array
# while also preserving the original shape (unlike just using boolean indexing).
# .where() function is a lot slower than boolean indexing
adults = np.where(ages >= 18, ages, 0)
# some also use -1, np.nan(np not a number) instead of 0.
print(adults)
# [[21  0 19 20  0 30 18 65]
#  [39 22  0 99 18 91 20 21]]