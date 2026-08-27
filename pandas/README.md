<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" width="320" alt="pandas logo">
</p>

<h1 align="center">pandas notes</h1>

<p align="center">
  <img src="https://img.shields.io/badge/topic-pandas-8A2BE2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/source-Bro%20Code-9370DB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/status-in%20progress-BA55D3?style=for-the-badge" />
</p>

> Still in progress. Covers series, dataframes, filtering, aggregate functions, groupby, and data cleaning so far. Will keep expanding as I get further into the video.

Notes and practice snippets from the Bro Code pandas video. Same as the numpy notes, this is a searchable dump for future me, not a docs page.

---

## What even is pandas

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

series2.loc["c"] = 200   # set value at label 'c'
series2.iloc[2] = 400    # set value at position 2
```

- `.loc[]` selects by label (the index name), not position, loc here means location, not locking a value
- `.iloc[]` selects by integer position, same idea as regular list indexing

### Filtering a series

Same trick as numpy boolean masking.

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

If you build a Series from a dict, the keys automatically become the index.

```python
calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}
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

> note to self: `.loc` uses labels, `.iloc` uses position. Easy to mix up when the index isn't just plain numbers.

---

## DataFrame

A DataFrame is a 2 dimensional table, rows and columns, basically an excel sheet in code form. There are two natural ways to build one, and it matters which shape your data is in:

```
dict of lists   ->  each list becomes a column   -> DataFrame
list of dicts   ->  each dict becomes a row       -> DataFrame
```

```python
data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50],
}
df = pd.DataFrame(data, index=['Employee 1', 'Employee 2', 'Employee 3'])
```

Adding a column is just assigning a list to a new key:
```python
df["job"] = ['Cook', 'N/A', "Cashier"]
```

Adding rows needs `pd.concat()`, and it wants a list of dataframes, not just one on its own:
```python
new_rows = pd.DataFrame([{'Name': 'Sandy', 'Age': 28, 'job': 'Engineer'},
                         {'Name': 'Mr.Crabs', 'Age': 60, 'job': 'Manager'}],
                         index=["Employee 4", "Employee 5"])
df = pd.concat([df, new_rows])
```

> `pd.concat()` wants a **list** of dataframes, tripped on this the first time.

---

## Reading data + selection

```python
df = pd.read_csv("pandas/pokemon_data.csv", index_col="Pokemon")
```

- `index_col` tells pandas which column becomes the row labels instead of the default 0-based index
- `pd.read_json()` works the same way for json files

Selection techniques covered so far:

| technique | what it does |
|---|---|
| `df["col"]` | single column |
| `df[["col1", "col2"]]` | multiple columns |
| `df.loc['row']` | row by label |
| `df.loc['row', ['col1', 'col2']]` | specific columns of a specific row |
| `df.loc['row1':'row2', ['col']]` | a range of rows by label, end is **inclusive** here (unlike normal python slicing) |
| `df.iloc[0:11:2, 0:3]` | rows/columns by integer position, works just like numpy slicing |

---

## Logical operators in pandas

Filtering with more than one condition needs pandas' own operators, not python's plain `and` / `or` / `not`.

| operator | meaning |
|---|---|
| `&` | AND |
| `\|` | OR |
| `~` | NOT |

```python
water_pokemon = df[(df["Type 1"] == "Water") | (df["Type 2"] == "Water")]
fire_pokemon = df[(df["Type 1"] == "Fire") & (df["Type 2"] == "Flying")]
print(fire_pokemon)
```
```
          Type 1  Type 2  Height  Weight  Legendary
Pokemon
Charizard   Fire  Flying     1.7    90.5          0
Moltres     Fire  Flying     2.0    60.0          1
```

> always wrap each condition in its own parentheses. Pandas evaluates `&` `|` `~` before comparisons, so without parentheses the expression breaks in confusing ways.

Other filters from the same section, kept simple, just a condition inside `df[...]`:

```python
tall_pokemon = df[df["Height"] >= 2]
heavy_pokemon = df[df["Weight"] > 100]
legendary_pokemon = df[df["Legendary"] == 1]  # same as == True
```

---

## Aggregate functions

Aggregate functions reduce a column (or the whole dataframe) down to a single summary value. Often paired with `groupby`.

```python
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
```
```
Height        1.671429
Weight       83.714286
Legendary     0.428571
dtype: float64
Height        11.7
Weight       586.0
Legendary      3.0
dtype: float64
```

Same functions work on a single column too:
```python
print(df["Height"].mean())  # 1.6714285714285713
print(df["Height"].sum())   # 11.7
```

Other aggregates that work the same way: `.min()`, `.max()`, `.count()`.

---

## GroupBy

`groupby` splits the dataframe into groups based on a column's values, then you run aggregate functions per group instead of over the whole thing.

```python
group = df.groupby("Type 1")
group["Height"].mean()   # average height, per type
group["Height"].sum()
group["Height"].min()
group["Height"].max()
group["Height"].count()
```

Think of it as "for every unique value in this column, give me a mini dataframe, then aggregate each one separately."

---

## Data cleaning

This is apparently the part that matters most in real world pandas work, a huge chunk of actual data work is just cleaning: fixing or removing incomplete, incorrect, or irrelevant data.

**Dropping irrelevant columns**
```python
df = df.drop(columns=['Legendary'])
```

**Handling missing data**
```python
df = df.dropna(subset=["Type 2"])  # restricts the missing-value check to this column only
df = df.fillna({'Type 2': "None"})  # or fill instead of drop
```

**Fixing inconsistent values**
```python
df['Type 1'] = df["Type 1"].replace({'Grass': 'GRASS', 'Fire': 'FIRE', 'Water': 'WATER'})
```

**Standardizing text**
```python
df['Pokemon'] = df['Pokemon'].str.lower()
```

**Fixing a column's data type**
```python
df["Legendary"] = df["Legendary"].astype(bool)
```

**Removing duplicate rows**
```python
df = df.drop_duplicates()
```

Full run showing duplicates before and after:
```
     Pokemon    Type 1  Type 2  Height  Weight  Legendary
0    pikachu  Electric     NaN     0.4     6.0      False
1  charizard      Fire  Flying     1.7    90.5      False
2  blastoise     Water     NaN     1.6    85.5      False
3   venusaur     Grass  Poison     2.0   100.0      False
4     mewtwo   Psychic     NaN     2.0   122.0       True
5    moltres      Fire  Flying     2.0    60.0       True
6     mewtwo   Psychic     NaN     2.0   122.0       True    <- duplicate row

after drop_duplicates():
     Pokemon    Type 1  Type 2  Height  Weight  Legendary
0    pikachu  Electric     NaN     0.4     6.0      False
1  charizard      Fire  Flying     1.7    90.5      False
2  blastoise     Water     NaN     1.6    85.5      False
3   venusaur     Grass  Poison     2.0   100.0      False
4     mewtwo   Psychic     NaN     2.0   122.0       True
5    moltres      Fire  Flying     2.0    60.0       True    <- row 6 gone
```

---

## Still to cover

- more groupby patterns (multiple aggregates at once, grouping by multiple columns)
- merging/joining multiple dataframes
- whatever's left in the video

---

## LC Questions

Pandas problems from LeetCode, practiced alongside the video content. Solutions live in [`LC_Questions/`](./LC_Questions).

### [595. Big Countries](./LC_Questions/595_big_countries.py)

Video walkthrough: [LeetCode 595 - Big Countries](https://youtu.be/VXtjG_GzO7Q?si=32zj5VXgKL4BGsBE)

```python
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world["population"] >= 25000000) | (world["area"] >= 3000000)][["name", "population", "area"]]
```

A country counts as "big" if population is at least 25,000,000 **or** area is at least 3,000,000. Straightforward use of the `|` operator covered above, filter first with the OR condition, then select just the columns the problem wants.