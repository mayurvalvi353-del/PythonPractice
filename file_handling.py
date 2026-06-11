with open("data.txt", "r") as file :  #For opening a file
    data = file.read()  #For reading a file

print(data)  #For printing data of that File

with open('students.txt', 'w') as f:
    f.write('Rahul Sharma, 85, Bhopal\n') #For writing data in file
    f.write('Priya Verma, 92, Indore\n')
    f.write('Amit Kumar, 73, Jabalpur\n')

with open('students.txt', 'a') as f:
    f.write('Sneha Joshi, 88, Indore\n')  #For adding or update new data in file

with open('students.txt', 'r') as f:
    content = f.read()
print(content)

with open('students.txt', 'r') as f: #Read line by line (memory efficient for large files)
    for line in f:
        name, marks, city = line.strip().split(',')
        print(f'{name:<15} | {marks:>5} | {city}')
        print("--------------")

#Creating a csv file
import csv

records = [
    ['Name', 'Marks', 'City', 'Grade'],
    ['Mayur', 85, 'Indore', 'B'],
    ['Dhruv', 92, 'Nashik', 'A'],
    ['Kavish', '73', 'Bhopal', 'B']
]

with open('students.csv', 'w', newline='') as f: #Writing data in csv file
    csv.writer(f).writerows(records)

with open('students.csv', 'r') as f: #Reading data in csv file
    for row in csv.DictReader(f):
        print(f'{row["Name"]}: {row["Marks"]} marks ({row["City"]})')

import csv

result = [
    ['Name', 'Age', 'Marks1', 'Marks2', 'Marks3' ],
    ['Mayur', 20, 73, 65, 89],
    ['Dhruv', 21, 78, 54, 63],
    ['Kavish', 19, 57, 63, 84]
]

with open('students_result.csv', 'w', newline='') as f: 
    csv.writer(f).writerows(result)

student = input("Enter the student's name : ")
found = False

with open('students_result.csv', 'r') as f: 
    for row in csv.DictReader(f):
        if row["Name"] == student :
            print(f'Found {student}')
            print(f'{row["Name"]}: Age : {row["Age"]}, marks 1 : {row["Marks1"]}, marks 2 : {row["Marks2"]}, marks 3 : {row["Marks3"]}')
            found = True
            break

if not found :
    print("Student Not found!")