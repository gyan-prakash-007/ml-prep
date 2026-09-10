<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" width="320" alt="pandas logo">
</p>

<h1 align="center">pandas notes</h1>

<p align="center">
  <img src="https://img.shields.io/badge/topic-pandas-8A2BE2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/source-Bro%20Code-9370DB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/status-in%20progress-BA55D3?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LeetCode-Introduction%20to%20Pandas-9932CC?style=for-the-badge" />
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

### [595. Big Countries](./LC_Questions/595_%20Big_Countries.py)

Video walkthrough: [LeetCode 595 - Big Countries](https://youtu.be/VXtjG_GzO7Q?si=32zj5VXgKL4BGsBE)

```python
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world["population"] >= 25000000) | (world["area"] >= 3000000)][["name", "population", "area"]]
```

A country counts as "big" if population is at least 25,000,000 **or** area is at least 3,000,000. Straightforward use of the `|` operator covered above, filter first with the OR condition, then select just the columns the problem wants.

### [2878. Get the Size of a DataFrame](./LC_Questions/2878_size_of%20data%20frame.py)

`.shape` is a property (not a method, so no parentheses) that returns a tuple of `(rows, columns)` for a dataframe or series. Quick way to check dimensions without counting anything manually.

```python
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
```

### [2879. Display the First Three Rows](./LC_Questions/2879_display_the%20first_3_rows.py)

```python
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
```

`.head(n)` grabs the first n rows, the pandas equivalent of `LIMIT 3` in SQL. About as simple as these problems get.

### [2880. Select Data](./LC_Questions/2880_selecting_data.py)

```python
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id'] == 101][['name', 'age']]
```

Filter rows first with a condition, then chain `[[...]]` to select just the columns you want, same pattern from the selection table earlier, just filter + column select combined in one line.

### [2881. Create a New Column](./LC_Questions/2881_create_new_column.py)

```python
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees['salary'] * 2
    return employees
```

Assigning to a new column key adds it to the dataframe, same pattern as the `df["job"] = [...]` example earlier in these notes.

### [2882. Drop Duplicate Rows](./LC_Questions/2882_drop_duplicate_row.py)

```python
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset='email')
```

Same `drop_duplicates()` from the data cleaning section, just scoped to one column with `subset`, so duplicates are judged only by email instead of the whole row.

### [2883. Drop Missing Data](./LC_Questions/2883_drop_missing_data.py)

```python
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset='name')
```

Same idea as `dropna()` from the cleaning section, `subset` limits the missing-value check to just the `name` column instead of scanning the whole dataframe.

### [2884. Modify Columns](./LC_Questions/2884_modify_columns.py)

```python
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees
```

Same column reassignment pattern as before, just overwriting an existing column instead of creating a new one.

### [2885. Rename Columns](./LC_Questions/2885_rename_columns.py)

`.rename(columns={...})` takes a dict mapping old column names to new ones and returns a dataframe with those columns renamed. Doesn't touch any other column.

```python
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={'id': 'student_id',
                                     'first': 'first_name',
                                     'last': 'last_name',
                                     'age': 'age_in_years'})
```

### [2886. Change Data Type](./LC_Questions/2886_change_type.py)

```python
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students
```

Same `.astype()` used earlier to convert `Legendary` to bool, here converting a column to `int` instead.

### [2887. Fill Missing Data](./LC_Questions/2887_fill_missing_data.py)

```python
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products
```

Same `.fillna()` from the cleaning section, this time filling a single column directly with a scalar (0) instead of passing a dict of column-to-value mappings.

### [2888. Reshape Data: Concatenate](./LC_Questions/2888_reshape_data.py)

```python
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df1 = pd.concat([df1, df2])
    return df1
```

Same `pd.concat()` used to add new rows earlier, just stacking two full dataframes on top of each other here instead of a dataframe and a couple of new rows.

### [2889. Reshape Data: Pivot](./LC_Questions/2889_pivot.py)

`.pivot()` reshapes long data into wide data: pick one column to become the new row index, another to become the new column headers, and a third to fill in the actual values. Turns repeated rows into a proper grid.

```python
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')
```

So a table with one row per (month, city, temperature) combo becomes a grid with months as rows, cities as columns, and temperature filling the cells.

### [2890. Reshape Data: Melt](./LC_Questions/2890_melt.py)

`.melt()` is the reverse of pivot, it takes wide data (lots of columns) and turns it into long data (fewer columns, more rows). `id_vars` is the column(s) to keep as-is, the rest get collapsed into a `var_name` (what the column used to be called) and a `value_name` (what value was in that column).

```python
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(
        id_vars=['product'],
        var_name='quarter',
        value_name='sales'
    )
```

So columns like `Q1`, `Q2`, `Q3`, `Q4` become rows instead, each with a `quarter` label and a `sales` value, keeping `product` fixed per row.

### [2891. Method Chaining](./LC_Questions/2891_method_chaining.py)

`.sort_values('col', ascending=False)` sorts the dataframe by a column, biggest first when `ascending=False`. Method chaining just means calling several operations back to back on the same line, filter then sort then select, instead of storing each step in its own variable.

```python
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values('weight', ascending=False)[['name']]
```

Filter to animals over 100 weight, sort heaviest to lightest, then keep only the `name` column, all in one chained line.