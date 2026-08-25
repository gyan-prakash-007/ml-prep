<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" width="320" alt="pandas logo">
</p>

<h1 align="center">pandas notes</h1>

<p align="center">
  <img src="https://img.shields.io/badge/topic-pandas-8A2BE2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/source-Bro%20Code-9370DB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/status-in%20progress-BA55D3?style=for-the-badge" />
</p>

> Work in progress. Halfway through the Bro Code pandas video, this README and the code file will get cleaned up and expanded once I finish. Publishing now just to keep the streak alive.

Notes and practice snippets from the Bro Code pandas video. Same as the numpy notes, this is just a searchable dump for future me, not a docs page.

---

## What even is pandas

Pandas gives you two main structures to work with:

```
Series      -> 1 dimensional, like a single column in a spreadsheet
DataFrame   -> 2 dimensional, like a full spreadsheet with rows and columns
```

Numpy is about raw arrays and math, pandas is built for actual tabular data, think CSVs, spreadsheets, tables with labeled rows and columns instead of just numbers by position.

---

## Series

A Series is a 1 dimensional labeled array that can hold any data type.

```python
data1 = [100.4, 102.2, 104.3]
series2 = pd.Series(data1, index=['a', 'b', 'c'])  # custom indexing

print(series2.loc['a'])
```
```
100.4
```

- `.loc[]` selects by label (the index name), not position, "loc" here means location, not locking a value
- `.iloc[]` selects by integer position, same idea as regular list indexing

```python
series2.loc["c"] = 200   # set value at label 'c'
series2.iloc[2] = 400    # set value at position 2 (same cell in this case)
```

### Filtering a series

Same trick as numpy boolean masking, works here too.

```python
data = [100, 102, 104, 200, 202]
series = pd.Series(data, index=["a", "b", "c", "d", "e"])
print(series[series >= 200])
```
```
d    200
e    202
dtype: int64
```

### Series from a dictionary

If you build a Series from a dict, the keys automatically become the index. Handy.

```python
calories = {
    "Day 1": 1750,
    "Day 2": 2100,
    "Day 3": 1700,
}

series = pd.Series(calories)
print(series)
print(series.loc["Day 2"])
```
```
Day 1    1750
Day 2    2100
Day 3    1700
dtype: int64
2100
```

Updating a value through `.loc` works like a normal dictionary/array update:

```python
series.loc["Day 3"] += 500
print(series)
```
```
Day 1    1750
Day 2    2100
Day 3    2200
dtype: int64
```

> note to self: `.loc` uses labels, `.iloc` uses position. Easy to mix up when the index isn't just plain numbers.

---

## DataFrame

A DataFrame is a 2 dimensional table, rows and columns, basically an excel sheet in code form.

There are two natural ways to build one, and it matters which shape your data is in:

```
dict of lists   ->  each list becomes a column   -> DataFrame
list of dicts   ->  each dict becomes a row       -> DataFrame
```

### Creating a DataFrame (dict of lists)

```python
data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50],
}

df = pd.DataFrame(data)
print(df)
```
```
        Name  Age
0  Spongebob   30
1    Patrick   35
2  Squidward   50
```

Custom row labels instead of the default 0, 1, 2 index:

```python
df = pd.DataFrame(data, index=['Employee 1', 'Employee 2', 'Employee 3'])
print(df)
```
```
                 Name  Age
Employee 1  Spongebob   30
Employee 2    Patrick   35
Employee 3  Squidward   50
```

```python
print(df.loc['Employee 1'])   # select by custom label
print(df.iloc[1])             # select by position
```
```
Name    Spongebob
Age            30
Name: Employee 1, dtype: object
Name    Patrick
Age          35
Name: Employee 2, dtype: object
```

### Adding a column

Just assign a list to a new key, same as adding a dict entry.

```python
df["job"] = ['Cook', 'N/A', "Cashier"]
print(df)
```
```
                 Name  Age      job
Employee 1  Spongebob   30     Cook
Employee 2    Patrick   35      N/A
Employee 3  Squidward   50  Cashier
```

### Adding rows (list of dicts)

```python
new_rows = pd.DataFrame([{'Name': 'Sandy', 'Age': 28, 'job': 'Engineer'},
                         {'Name': 'Mr.Crabs', 'Age': 60, 'job': 'Manager'}],
                         index=["Employee 4", "Employee 5"])

df = pd.concat([df, new_rows])
print(df)
```
```
                 Name  Age       job
Employee 1  Spongebob   30      Cook
Employee 2    Patrick   35       N/A
Employee 3  Squidward   50   Cashier
Employee 4      Sandy   28  Engineer
Employee 5   Mr.Crabs   60   Manager
```

> `pd.concat()` wants a list of dataframes, not just one dataframe on its own. Tripped on this the first time.

---

## Reading data from files

```python
df = pd.read_csv("pandas/pokemon_data.csv", index_col="Pokemon")
print(df)
```
```
               Type  Height  Weight
Pokemon
Pikachu    Electric     0.4     6.0
Charizard      Fire     1.7    90.5
Blastoise     Water     1.6    85.5
Venusaur      Grass     2.0   100.0
```

- `index_col` tells pandas which column to use as the row labels instead of the default 0-based index
- there's also `pd.read_json()` for json files, same idea

### Selection techniques so far

```python
print(df.loc['Pikachu'])                        # a whole row by label
print(df.loc['Charizard', ['Height', 'Weight']]) # specific columns of a specific row
```
```
Type      Electric
Height         0.4
Weight         6.0
Name: Pikachu, dtype: object
Height     1.7
Weight    90.5
Name: Charizard, dtype: float64
```

Column selection (`df["col"]`, `df[["col1", "col2"]]`) came up in the video too, notes on that coming once I actually get further into the selection section properly.

---

## Still to cover

- column selection in more depth (single vs multiple columns)
- filtering dataframes by condition, not just series
- sorting, grouping, more of the real analysis side of pandas

This section will get filled in and the whole file polished once the video's done.