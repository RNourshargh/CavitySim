import numpy as np
import pandas as pd

# THe cavity length and scope time scaling have both been fudged. There isn't actually any fitting happening yet

def import_octascope_csv(filepath,):
    """
    Use Pandas to import the octascope to a data frame.
    
    filepath: Location of the CSV to import
    """
    return
    
my_dict = { 'name' : ["a", "b", "c", "d", "e"],
                   'age' : [20,27, 35, 55, 18],
                   'designation': ["VP", "CEO", "CFO", "VP", "VP"]}

df = pd.DataFrame(my_dict,
index = [
"First -> ",
"Second -> ", 
"Third -> ", 
"Fourth -> ", 
"Fifth -> "]
)   

series_name = df.name
series_age = df.age

print(series_age.tolist())
series_designation = df.designation

series_col = []

df_from_series = pd.DataFrame(series_name)

t_dict = {'a' : [1,2,3], 'b': [4,5], 'c':6, 'd': "Hello World"}

ds = pd.DataFrame([t_dict, t_dict ], index=[1,2])

#print(ds)

# my_list = [[1,2,3,4],
           # [5,6,7,8],
           # [9,10,11,12],
           # [13,14,15,16],
           # [17,18,19,20]]
# #df = pd.DataFrame(my_dict)


# #df = pd.DataFrame(my_list)
# # df = pd.DataFrame(
# # my_list, 
# # index = ["1->", "2->", "3->", "4->", "5->"], 
# # columns = ["A", "B", "C", "D"]
# # )

# np_arr = np.array([[1,2,3,4],
                   # [5,6,7,8],
                   # [9,10,11,12],
                   # [13,15,16,16],
                   # [17,18,19,20]])
# df = pd.DataFrame(np_arr)

# output = df+100

