#Introduction to pandas and numpy
#Pandas is a python library for data manipulation

import pandas as pd
import numpy as np

#The basic unit of analysis in pandas is the dataframe: rows and columns: two dimensional array

#Let's look at pd.series
#A series is a one-dimensional array of values  

#Let's create a pd.series
#Documentation

ps = (['a',1,2,np.pi])
print(ps)

#Which data type does our pd.Series have?
print(type(ps))

#numpy is one of the reason why python became popular: it is a very fast linear algebra library

# Define a custom index
series_1 = pd.Series(
  data = ["Schnitzel","Lemonade","Whiskey"],
  index = ["Food","Soda","Alcohol"],
 )

#Advanced indexing of pd.Series
#using .loc[]

series_1.loc["Food"]

print(series_1.loc[["Food","Alcohol"]])

#Using .iloc[]

#Pandas allows us to retrieve a range of values using .iloc[]

#Access elements from a range of indexes

print(series_1.loc["Food:"Alcohol"])])

  