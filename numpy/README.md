<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg" width="280" alt="numpy logo">
</p>

<h1 align="center">numpy notes</h1>

<p align="center">
  <img src="https://img.shields.io/badge/topic-numpy-8A2BE2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/source-Bro%20Code-9370DB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/status-done-BA55D3?style=for-the-badge" />
</p>

Quick notes and practice snippets from the Bro Code numpy video. This isn't a docs page, just me dumping stuff here so future me can search it instead of rewatching an hour long video for one line of syntax.

Video: [Learn Numpy in 1 Hour - Bro Code](https://youtu.be/VXU4LSAQDSc?si=9GKsNppKbEEjDcw3)

---

## What even is numpy

Numpy = **num**erical **py**thon. It gives you the `ndarray` (n-dimensional array), which is basically a python list on steroids: faster, and supports proper math operations on the whole array at once instead of looping through it.

```python
import numpy as np

array = np.array([1, 2, 3, 4])
array = array * 2
print(array)
```
```
[2 4 6 8]
```

Notice it multiplied *every* element by 2 with no loop needed. That's the whole point of numpy honestly, vectorized operations instead of manual for-loops.

---

## Dimensions

Arrays can be 0-D (a single value), 1-D (a list), 2-D (a table/matrix), or go even higher (3-D, 4-D...). Once you're past 2-D just think of it as "array of arrays of arrays."

```python
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                   [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                   [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]])

print(array.ndim)   # number of dimensions
print(array.shape)  # (depth, rows, columns)
```
```
3
(3, 3, 3)
```

**Indexing:** you can chain-index like `array[0][0][0]`, but `array[0, 0, 0]` (comma style) is faster and is the numpy way to do it.

> note to self: shape tells you the *size* along each axis, ndim tells you *how many* axes there are. Easy to mix these up.

---

## Slicing

Same idea as python list slicing (`start:end:step`), just extended across rows and columns.

```python
array = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

print(array[::-1])      # reverse all rows
print(array[:, 0])      # first column
print(array[:, ::-1])   # reverse column order
print(array[0:2, 0:2])  # top-left 2x2 block
```
```
[[13 14 15 16]
 [ 9 10 11 12]
 [ 5  6  7  8]
 [ 1  2  3  4]]
[ 1  5  9 13]
[[ 4  3  2  1]
 [ 8  7  6  5]
 [12 11 10  9]
 [16 15 14 13]]
[[1 2]
 [5 6]]
```

- `array[row_start:row_end:row_step, col_start:col_end:col_step]`
- comma splits rows and columns, the `:` alone before the comma means "give me all rows"
- end index is always exclusive, classic python behaviour

---

## Scalar and element-wise arithmetic

```python
array = np.array([1, 2, 3])
print(array + 1)  # [2 3 4]
print(array ** 5) # [  1  32 243]
```

Scalar math applies to every element automatically. Same goes for two arrays of the same shape:

```python
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print(array1 + array2)  # [5 7 9]
print(array1 * array2)  # [ 4 10 18]
```

No loops, no `zip()`, just plain `+` and `*` and numpy handles it element by element.

---

## Vectorized math functions

```python
array = np.array([1.01, 2.5, 3.99])
print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))
```
```
[1.00498756 1.58113883 1.99749844]
[1. 2. 4.]
[1. 2. 3.]
[2. 3. 4.]
```

Also has constants like `np.pi`. Used it for a quick exercise, area of circles given an array of radii:

```python
radius = np.array([1, 2, 3])
print(np.pi * radius ** 2)
```
```
[ 3.14159265 12.56637061 28.27433388]
```

---

## Comparison operators and masking

Comparing an array against a number gives you back a boolean array. That boolean array can then be used to filter or replace values, this is called masking.

```python
scores = np.array([91, 55, 100, 73, 82, 64])
print(scores >= 60)

scores[scores < 60] = 0  # replace every score below 60 with 0
print(scores)
```
```
[ True False  True  True  True  True]
[ 91   0 100  73  82  64]
```

This one clicked for me, `scores < 60` returns `[True, True, ...]` and numpy uses that as a mask to pick which elements to overwrite. No loop, no if-else.

---

## Broadcasting

This is the one that felt like magic at first. Broadcasting lets numpy do math between arrays of *different* shapes by stretching the smaller one to match, as long as:

- the dimensions match, or
- one of them is size 1

```python
array1 = np.array([[1, 2, 3, 4]])   # shape (1, 4)
array2 = np.array([[1], [2], [3], [4]])  # shape (4, 1)

print(array1 * array2)
```
```
[[ 1  2  3  4]
 [ 2  4  6  8]
 [ 3  6  9 12]
 [ 4  8 12 16]]
```

A row vector times a column vector gives you a full matrix, this is basically how you'd generate a multiplication table with zero loops:

```python
array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(array1 * array2)
```
```
[[  1   2   3   4   5   6   7   8   9  10]
 [  2   4   6   8  10  12  14  16  18  20]
 [  3   6   9  12  15  18  21  24  27  30]
 ...
 [ 10  20  30  40  50  60  70  80  90 100]]
```

> broadcasting = free multiplication tables. neat trick, remember this one for interviews.

---

## Aggregate functions

Functions that collapse the whole array down to one summary value (or one per row/column if you use `axis`).

| function | what it does |
|---|---|
| `np.sum()` | adds everything up |
| `np.mean()` | average |
| `np.median()` | middle value |
| `np.min()` / `np.max()` | smallest / largest |
| `np.argmin()` / `np.argmax()` | index of smallest / largest |
| `np.std()` / `np.var()` | standard deviation / variance |

```python
array = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10]])

print(np.sum(array, axis=0))  # sum down each column
print(np.sum(array, axis=1))  # sum across each row
```
```
[ 7  9 11 13 15]
[15 40]
```

> axis=0 goes down (column-wise), axis=1 goes across (row-wise). I keep forgetting this so writing it down properly this time.

---

## Filtering (boolean indexing)

```python
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                  [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
```
```
teenagers: [17 16 15 18]
adults:    [21 19 20 30 18 39 22 18 19 20 21]
```

Boolean indexing like this flattens the array, you lose the original shape. Use `&` and `|` instead of python's `and`/`or` since numpy compares element by element (C-style operators).

If you want to keep the original shape while filtering, use `np.where`:

```python
adults = np.where(ages >= 18, ages, 0)
```
This keeps every value that passes the condition, and replaces the rest with 0 while keeping the same 2D shape.

---

## Random numbers

```python
rng = np.random.default_rng(seed=1)
print(rng.integers(low=1, high=109, size=(3, 2)))

rng.shuffle(array)  # shuffles in place

fruits = np.array(["apple", "orange", "banana", "coconut"])
print(rng.choice(fruits, size=(3, 2)))
```

- `default_rng()` is the modern way to generate random numbers in numpy (the newer Generator API), old-school `np.random.seed()` + `np.random.uniform()` still works but generator style is preferred now
- passing a `seed` makes the randomness reproducible, useful for debugging

---

