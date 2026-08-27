# pandas = panel data
# pandas works with series and dataframes
# series is one dimensional tabular data
# dataframe is two dimensional data
# with pandas we can export, display, and tabulate data

import pandas as pd

# series = a pandas 1 dimensional labeled array that can hold any data type
# (think of it as a single column spreadsheet)

data1 = [100.4, 102.2, 104.3]
data2 = ['A', 'B', 'C']
data3 = [True, False, True]

series1 = pd.Series(data3)  # creates a series with default indexing from 0 to n
series2 = pd.Series(data1, index=['a', 'b', 'c'])  # custom indexing

print(series2.loc['a'])
# series.loc[] is a property used to select, filter, and modify data in a
# dataframe or series using row and column labels (names) or boolean arrays

series2.loc["c"] = 200  # locate the value at index c and modify it to 200, loc means location not locking a value
series2.iloc[2] = 400   # iloc is integer location, like normal indexing, this modifies the 2nd index element

# filtering by value
data = [100, 102, 104, 200, 202]
series = pd.Series(data, index=["a", "b", "c", "d", "e"])
print(series[series >= 200])

# filtering by index
calories = {
    "Day 1": 1750,
    "Day 2": 2100,
    "Day 3": 1700,
}

series = pd.Series(calories)  # for a key value pair like a dictionary, the keys become the index automatically
print(series)
print(series.loc["Day 2"])  # can access data using loc

series.loc["Day 3"] += 500  # updating the value at key Day 3 using loc
print(series)

# filtering by value
print(series[series >= 2000])
print(series[series < 2000])

# exercise 1: create a series of pokemon with keys being its type

pokemon = {
    "Fire": "Charizard",
    "Water": "Blastoise",
    "Grass": "Venusaur",
    "Electric": "Pikachu",
    "Psychic": "Mewtwo",
    "Ice": "Articuno",
    "Rock": "Onix",
    "Ground": "Garchomp",
    "Dragon": "Dragonite",
    "Ghost": "Gengar"
}

pokemon_series = pd.Series(pokemon)
print(pokemon_series)

# dataframe = a tabular data structure with rows and columns (2 dimensional), similar to an excel spreadsheet

data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50],
}

df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, index=['Employee 1', 'Employee 2', 'Employee 3'])  # creating custom indexing
print(df)

print(df.loc['Employee 1'])  # selecting by custom indexing
print(df.iloc[1])            # indexing by numbers

# add a new column
df["job"] = ['Cook', 'N/A', "Cashier"]
print(df)

# add new rows
new_rows = pd.DataFrame([{'Name': 'Sandy',
                          'Age': 28,
                          'job': 'Engineer'},
                         {'Name': 'Mr.Crabs',
                          'Age': 60,
                          'job': 'Manager'}],
                         index=["Employee 4", "Employee 5"])

df = pd.concat([df, new_rows])  # concat needs a list of dataframes, not just one
print(df)

# dictionary of lists -> columns -> dataframe
# list of dictionaries -> rows -> dataframe

# exercise 2: creating a dataframe using pokemon data

pokemon = {
    "name": [
        "Pikachu", "Charizard", "Blastoise", "Venusaur", "Lucario",
        "Garchomp", "Greninja", "Sylveon", "Decidueye", "Dragapult"
    ],

    "type": [
        "Electric", "Fire", "Water", "Grass", "Fighting",
        "Dragon", "Water", "Fairy", "Grass", "Dragon"
    ],

    "region": [
        "Kanto", "Kanto", "Kanto", "Kanto", "Sinnoh",
        "Sinnoh", "Kalos", "Kalos", "Alola", "Galar"
    ]
}

df_pokemon = pd.DataFrame(pokemon, index=["Pokemon 1", "Pokemon 2", "Pokemon 3", "Pokemon 4", "Pokemon 5", "Pokemon 6", "Pokemon 7", "Pokemon 8", "Pokemon 9", "Pokemon 10"])
print(df_pokemon)

df_pokemon["Legendary"] = [False, False, False, False, False, False, True, False, False, False]

new_pokemon = [
    {"name": "Dialga", "type": "Steel/Dragon", "region": "Sinnoh", "legendary": True},
    {"name": "Palkia", "type": "Water/Dragon", "region": "Sinnoh", "legendary": True}
]

df_new_pokemon = pd.DataFrame(new_pokemon, index=['Pokemon 11', 'pokemon 12'])

df_pokemon = pd.concat([df_pokemon, df_new_pokemon])
print(df_pokemon)

# importing data from a csv file
df = pd.read_csv("pandas/pokemon_data.csv", index_col="Pokemon")  # set index column to Pokemon, default is 0 based indexing
print(df)

# reading a json file
# df = pd.read_json("pandas/pokemon_150.json", index_col="Pokemon")

# different selection techniques

# selection by column
# print(df["Pokemon"])
# print(df['Weight'])

# selecting multiple columns
# print(df[["Pokemon", "Height", "Weight"]])

# selection by rows
print(df.loc['Pikachu'])
print(df.loc['Charizard', ['Height', 'Weight']])