#use #%% to create cells for cell by cell exection and debugging
import os
import pandas as pd
import matplotlib as mlt
import numpy as np

#set a working directory first
os.chdir("E:\DATA SCIENCE PREPERATION\EDWISOR\Dataset_library")

#check the current working directory
os.getcwd()
#%%
#load a CSV file in python
df_csv = pd.read_csv("mt_cars.csv", sep=',')
#check if loaded properly:
#print(df_csv)

#load a excel file in python
df_xl = pd.read_excel("mt_cars.xlsx")

#instead of print you can just type the varible in df_xl in console 
#to see the display as well
#%%
#check the column names from CSV file
print(df_xl.columns)

# type would tell the type of dataset loaded and is dataframe or not
# this tells us the structure of the dataset
print(type(df_xl))

# To get a summary of the number of variables and observations ini a dataset
print(df_xl.shape)
#(32,11) here we have 32 observations(rows) and 11 variables(columns)

#Getting the first 10 rows of a dataset just like we did in R.
# by default the head function returns 5 observations (rows)
print(df_xl.head())

#we can pass variable argument of the number of rows we want to fetch
# in the head function as shown below:
print(df_xl.head(20))


# to get the last 10 rows of the data set, default function returns last 5 rows
#can pass argument in the tail function as well just like in head
print("tail")
print(df_xl.tail())
print(df_xl.tail(10))

#delete a dataframe -(dataset)
del df_xl
#print(df_xl)

#reloading the xlsx
df_xl = pd.read_excel("mt_cars.xlsx")

#%%
#slice and dice the dataframe to your needs using iLoc
#something noteworthy:-
#please note that the dataframe is loaded in python from 0 index
# now when iloc is used, 
#for first argument passed in iloc - 
#it will fetch array position 5,to array position 10 - for rows
#for second argument passed in iloc
#and array position 2,to array position 5 - for colums 
df_iloc = df_xl.iloc[5:10,2:5]
print(df_iloc)

#if no argument is passed in the first position it takes it as 0th
#position of the dataframe
df_iloc1 = df_xl.iloc[:10,:5]

#%%
#fetch unique values in a column - variable
# here we pass the name of the column in thrid braces single quotes
df_uniq = df_xl['cyl'].unique()
print(df_uniq)
#%%
#Fetch the count of observations grouped by the unique values of a column
df_count = df_xl['cyl'].value_counts()
print(df_count)
#%%
#various descriptive information would be given by describe 
# a summary of description for a column -variable
df_desc = df_xl['cyl'].describe()
print(df_desc)  
#%%
#simple assignment operations
var_num = 25
print(var_num)
var_string = 'I love India'
print(var_string)
#%%
#calculate mean from a particular column
df_mean = df_xl['cyl'].mean()
df_median = df_xl['cyl'].median()
df_variance = df_xl['cyl'].var()
df_standard_deviation = df_xl['cyl'].std()
df_sum = df_xl['cyl'].sum()
df_mode = df_xl['cyl'].mode()
#%%
# write the csv output converting from excel
#index = false removed the array index numbers from the output
df_xl.to_csv("mt_cars_xl_to_csv.csv", index=False)
#%%
# write the excel otuput converting from csv
#index = false removed the array index numbers from the output
df_csv.to_excel("mt_cars_csv_to_xl.xlsx", index=False)
#%%
























