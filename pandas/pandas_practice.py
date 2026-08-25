#  pandas = panal data
# pandas work with series and data frame 
# series is one dimentional tabular data 
# data prame is 2 dimensional data 
# with oanda wwe can export , display and tabulate data
import pandas as pd

# series = a pandas 1 dimesional labeled array that can hold any data type. (think of it as a single column spread sheet )

data1 =  [100.4,102.2,104.3]
data2 = ['A','B','C']
data3 = [True,False,True]

series1 = pd.Series(data3) # creates a series with default indexing from 0 to n 
series2 = pd.Series(data1, index=['a','b','c']) # custon indexing 

#print(series2)

print(series2.loc['a']) #series.loc[] is a property used to select, filter, and modify data in a DataFrame or Series using row and column labels (names) or boolean arrays

series2.loc["c"] = 200 # locating the value at index c and modifying it too 200 // loc here means location not locking value 
series2.iloc[2] = 400  # i loc is integer location like indexing we are modifying the 2nd index element with the help of iloc


#print(series2)

# filtering by value 
data =  [100,102,104,200,202]
series = pd.Series(data, index=["a","b","c","d","e"])

#print(series[series >= 200])


# filtering by index 
calories = {
    "Day 1" : 1750,
    "Day 2" : 2100,
    "Day 3" : 1700,
}

series  = pd.Series(calories) # for a key value pair like dictionary the keys become the index automatically
print(series) 
print(series.loc["Day 2"]) # can access data using loc 

series.loc["Day 3"] += 500 # updating the value at key day 3 using loc

print(series)

# filtering by value 
  
print(series[series>=2000])
print(series[series<2000])

# exercise 1 createte a series of pokemon with keys being its type 

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

# Dataframe = A tabular data structure with rows and columns (2.dimensional) similar to an excel spreadsheet 

data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30,35,50],
}

df = pd.DataFrame(data)

print(df)
#         Name  Age
# 0  Spongebob   30
# 1    Patrick   35
# 2  Squidward   50

df = pd.DataFrame(data, index=['Employee 1', 'Employee 2', 'Employee 3']) # creating custom indexing 
print(df)
#           Name  Age
# Employee 1  Spongebob   30
# Employee 2    Patrick   35
# Employee 3  Squidward   50

print(df.loc['Employee 1']) # selecting by custom indexing 
print(df.iloc[1]) # indexing by numbers

# add a new column 

df["job"] = ['Cook','N/A',"Cashier"]
print(df)

# add a new row 

new_rows = pd.DataFrame([{'Name': 'Sandy',
                         'Age':28,
                         'job': 'Engineer'},
                         {'Name': 'Mr.Crabs',
                         'Age':60,
                         'job': 'Manager'}],
                         index= ["Employee 4", "Employee 5"])

df = pd.concat([df,new_rows]) # concat function need list of df not just ddf
print(df)


# Dictionary of lists
#        ↓
#    Columns
#        ↓
# DataFrame

# List of dictionaries
#        ↓
#      Rows
#        ↓
# DataFrame

# exercise 2 creating data frame useing the pokemon data 

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

df_pokemon = pd.DataFrame(pokemon,index = ["Pokemon 1", "Pokemon 2", "Pokemon 3", "Pokemon 4", "Pokemon 5", "Pokemon 6", "Pokemon 7", "Pokemon 8", "Pokemon 9", "Pokemon 10"])

print(df_pokemon)

df_pokemon["Legendary"] = [False, False, False, False, False, False, True, False, False, False]

new_pokemon = [
    {"name": "Dialga", "type": "Steel/Dragon", "region": "Sinnoh", "legendary": True },
    {"name": "Palkia", "type": "Water/Dragon", "region": "Sinnoh", "legendary": True}
]

df_new_pokemon = pd.DataFrame(new_pokemon, index=['Pokemon 11', 'pokemon 12'])

df_pokemon = pd.concat([df_pokemon,df_new_pokemon])
print(df_pokemon)

# importing data csv file 
# reading json file 
df = pd.read_csv("pandas/pokemon_data.csv", index_col = "Pokemon") # setting the index column to pokemon comumn default is 0 based indexing 
print(df)

# reading json file 
#df = pd.read_json("pandas/pokemon_150.json",index_col = "Pokemon")

print(df)


# different selection techniques 

# SELECTION BY COLUMN 
#print(df["Pokemon"])
#print(df['Weight'])

# SELECTING multiple columns 
#print(df[["Pokemon", "Height","Weight"]])

# SELECTION BY ROWS

print(df.loc['Pikachu'])
print(df.loc['Charizard',['Height','Weight']])
