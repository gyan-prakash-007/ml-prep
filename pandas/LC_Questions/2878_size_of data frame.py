# 2878 get size of data frame 
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:

    return list(players.shape)

# shape is a property (attribute) used in the pandas library to quickly determine the dimensions of a DataFrame or Series