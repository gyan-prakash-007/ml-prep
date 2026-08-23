# numpy = numerical python

import numpy as np

# creating numpy arrays

array = np.array([1, 2, 3, 4])
array = array * 2
print(array)

print(type(array))  # <class 'numpy.ndarray'>

# multidimensional arrays in numpy

array = np.array('A')  # 0 dimensional array
array = np.array(['A', 'B', 'C'])  # 1 dimensional array
array = np.array([['A', 'B', 'C'],
                   ['D', 'E', 'F'],
                   ['G', 'H', 'I']])  # 2 dimensional array
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                   [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                   [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]])  # 3 dimensional array

print(array.ndim)   # returns the number of dimensions (axes) of a numpy array
print(array.shape)  # returns tuple (depth, rows, columns)

print(array[0][0][0])  # chain indexing

print(array[0, 1, 0])  # multidimensional indexing, faster than chain indexing

word = array[0, 0, 0] + array[2, 0, 0] + array[2, 0, 0]
print(word)

# slicing using numpy

array = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

# array[start:end:step]
# array[row_start:row_end:row_step, column_start:column_end:column_step]

# row selection
print(array[0])       # element at first index
print(array[-1])      # element at last index
print(array[0:3])     # end is exclusive, so this stops before index 3
print(array[::2])     # step through every second row
print(array[::-1])    # return all rows reversed

# column selection
print(array[:, 0])       # first column
print(array[:, -1])      # last column
print(array[:, 0:3])     # first 3 columns
print(array[:, 1:])      # all columns from the second onward
print(array[:, ::2])     # every second column
print(array[:, 1::2])    # every second column, starting from the second column
print(array[:, ::-1])    # reverse the order of columns

# row and column selection together
print(array[0:2, 0:2])  # rows 1-2 and columns 1-2
print(array[:2, 2:])    # first 2 rows, last columns of the selected rows
print(array[2:, :2])    # last 2 rows, first 2 columns
print(array[2:, 2:])    # last 2 rows, last 2 columns

# scalar arithmetic

array = np.array([1, 2, 3])
print(array + 1)   # adds 1 to every element
print(array - 2)   # subtracts 2 from every element
print(array * 3)   # multiplies every element by 3
print(array / 4)   # divides every element by 4
print(array ** 5)  # raises every element to the power of 5

# vectorized math functions

array = np.array([1.01, 2.5, 3.99])

print(np.sqrt(array))
print(np.round(array))  # round to nearest
print(np.floor(array))  # round down
print(np.ceil(array))   # round up

print(np.pi)  # returns the value of pi

# exercise 1: given an array of radii, get the corresponding array of areas
radius = np.array([1, 2, 3])
print(np.pi * radius ** 2)

# element wise arithmetic

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

# comparison operators

scores = np.array([91, 55, 100, 73, 82, 64])

print(scores == 100)
print(scores >= 60)
print(scores < 60)

scores[scores < 60] = 0  # replace every score below 60 with 0
print(scores)

# broadcasting

# broadcasting lets numpy perform operations on arrays with different shapes
# by virtually expanding dimensions so they match the larger array's shape.
#
# rules:
# - the dimensions are the same size
# - or one of the dimensions has a size of 1

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)
print(array2.shape)
print(array1 * array2)

# exercise 2: printing a multiplication table using broadcasting
array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(array1.shape)
print(array2.shape)
print(array1 * array2)

# aggregate functions

# aggregate functions summarize data and typically return a single value
#
# np.sum()             adds all elements
# np.prod()            multiplies all elements
# np.mean()            computes the arithmetic average
# np.median()          finds the middle value
# np.min() / np.max()  finds the smallest / largest value
# np.argmin() / np.argmax()  returns the index of the min / max value
# np.std() / np.var()  computes the standard deviation and variance

array = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.min(array))
print(np.max(array))
print(np.argmin(array))
print(np.argmax(array))

print(np.sum(array, axis=0))  # axis=0 applies the operation down the columns
print(np.sum(array, axis=1))  # axis=1 applies the operation across the rows

# filtering

# filtering refers to selecting elements from an array that match a given condition

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                  [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18]  # boolean indexing, this flattens the array
print(teenagers)

adults = ages[(ages >= 18) & (ages < 65)]  # numpy uses C-style & instead of "and"
print(adults)

seniors = ages[ages >= 65]
print(seniors)

evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]
print(odds)

# when filtering while wanting to preserve the shape of the original array, use np.where
# np.where(condition, value_if_true, value_if_false)
adults = np.where(ages >= 18, ages, 0)
print(adults)

# random number generation

rng = np.random.default_rng(seed=1)
print(rng.integers(low=1, high=109, size=(3, 2)))

np.random.seed(1)
print(np.random.uniform(low=-1, high=1, size=(3, 2)))

# shuffle an array
rng = np.random.default_rng()
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)

# random choice
fruits = np.array(["apple", "orange", "banana", "coconut"])
fruit = rng.choice(fruits, size=(3, 2))
print(fruit)