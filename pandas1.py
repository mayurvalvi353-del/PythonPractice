import pandas as pd

data = {
    'Name' : ['Suriya','Sameera','Vijay','Trisha','Vikram'],
    'Age' : [22,21,23,20,24],
    'Marks' : [85,92,78,88,73],
    'City' : ['Bhopal','Indore','Chennai','Indore','Bangalore']
}
df = pd.DataFrame(data)
print(df)

print(df.shape) #Returns shape of df or no. of rows and columns

print(df.head(3)) #Returns First 3 rows

print(df.dtypes) #Data types of each column

print(df.describe()) #Statistical Summary

#Select columns
print("df['Name'] : \n", df['Name'])
print(df[['Name', 'Marks']])

#Filter rows
print(df[df['Marks'] >= 85])
print(df[df['City'] == 'Bhopal'])
print(df[(df['Marks'] >= 80) & (df['City'] == 'Indore')]) #Multiple Conditions

def get_grade(x):
    if x >= 90 :
        return 'A'
    elif x >= 75 :
        return 'B'
    else :
        return 'C'
    
df['Grade'] = df['Marks'].apply(get_grade) #Adding Grade column 
print(df['Grade'])
print("---------------------------------")
print(df)

#GroupBy - like Excel pivot
city_avg = df.groupby('City')['Marks'].mean()
print(city_avg)

#Read Real Csv file
df2 = pd.read_csv('students.csv')
#Cleaning
df2['Name'] = df2['Name'].str.strip()
df2['Marks'] = df2['Marks'].str.replace('#', '')
df2.to_csv('clean_output.csv', index = False)  #Save
print(df2)


