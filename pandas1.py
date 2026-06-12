import pandas as pd

data = {
    'Name' : ['Suriya','Sameera','Vijay','Trisha','Vikram'],
    'Age' : [22,21,23,20,24],
    'Marks' : [85,92,78,88,73],
    'City' : ['Bhopal','Indore','Chennai','Hyderabad','Bangalore']
}
df = pd.DataFrame(data)
print(df)

print(df.shape) #Returns shape of df or no. of rows and columns

print(df.head(3)) #Returns First 3 rows

print(df.dtypes) #Data types of each column

print(df.describe()) #Statistical Summary