import pandas as pd
import numpy as np

#create some data
data={'Tokyo':30_000_000,
     'Delhi':50_000_000,
     'Shanghai':20_000_000,}

#We can use underscores to use the numbers more readable

df = pd.DataFrame(data = data, index=[0,1,2])

print(df)


#Create a dataframe from a cvs.file

#Access number of rows
#print(df_raw.shape[0])

#Access number of columns

#print(df_raw.shape[1])

#Access number of rows and columns

#print(df_raw.shape)

#Create multiple ways of doing so
#df.nightss = 1
#df['nnights'] = 1
#df = df_raw.assign(nnights = 1)

#Delete df_raw since we do not need it anymore

#del df_raw

#We want to clean this up
#df['accommodationtype'] = df['accommodationtype'].str.split(' ')

#df_raw['accommodationtype'] = df_raw['accommodationtype'].str.split('@').str[1]

#How many nights in each accommodationtype
#df_raw['accommodationtype'].value_counts()

#Clean up missing value
#df_raw.accommodationtype.replace("", "Unknmown", inplace = True)

#Check out the new variable

#df_raw['ratings'] = df_raw['guestreviewsratings].str.split('/').str[0]

#rename df_raw variable to df
df_raw = pd.read_csv('https://osf.io/yzntm/download')
df = df_raw

#rename guestreviewsratings to reviews
df.rename(columns={'guestreviewsratings':'reviews'}, inplace = True)

#convert the revies into float type variable
df['reviews'] = df['reviews'].astype(float)

#install matplot lib
#import matplotlib.pyplot as plt

#create a histogram of reviews
df['reviews'].hist()

#create a new variable distance_numeric
df['distance_numeric'] = df['distance'].str.replace('km','').astype(float)

