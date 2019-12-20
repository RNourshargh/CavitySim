import numpy as np
import pandas as pd

# THe cavity length and scope time scaling have both been fudged. There isn't actually any fitting happening yet


def import_octascope_csv(filepath,):
    """
    Use Pandas to import the octascope to a data frame.
    
    filepath: Location of the CSV to import
    """
    return


my_dict = {
    "name": ["a", "b", "c", "d", "e"],
    "age": [20, 27, 35, 55, 18],
    "designation": ["VP", "CEO", "CFO", "VP", "VP"],
}

#df_csv = pd.read_csv('csv_example', names=["a","b","c"], header=1)
#df.to_csv('csv_example', index=False)
df_csv = pd.read_csv( "PandasTestScope.csv", usecols=[0,1,2], header=None, skiprows=15)

print(df_csv)