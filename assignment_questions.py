#1
name = "Mayur Valvi"
age = 21
course = "B.Tech CSIT"

print("Name :",name,"\n""Age :", age,"\n""Course :", course)

#2
# Student 1 details
name1 = "Rahul"
age1 = 20
course1 = "Computer Science"

# Student 2 details
name2 = "Priya"
age2 = 21
course2 = "Mathematics"

# Student 3 details
name3 = "Amit"
age3 = 19
course3 = "Physics"

# Printing student details
print("Student 1:")
print("Name:", name1)
print("Age:", age1)
print("Course:", course1)

print("\nStudent 2:")
print("Name:", name2)
print("Age:", age2)
print("Course:", course2)

print("\nStudent 3:")
print("Name:", name3)
print("Age:", age3)
print("Course:", course3)

#3 
a = int(input("Enter the first integer :"))
b = int(input("Enter the second integer :"))

print("Sum :", a+b)

#4
c = float(input("Enter the first number :"))
d = float(input("Enter the second number :"))

print("Multiplication :", c*d)

#5
ch = input("Enter a character : ")

print("The ASCII value of character is :", ord(ch))

#6
num1 = 20
num2 = 30

sum = num1 + num2

print("Sum :", sum)

#7
e = 60
f = 20
diff = e - f
print("Difference : ", diff)

#8
h = 12
g = 5
product = h*g
print("Multplication :", product)

#9
i = 32
j = 8
quotient = i/j
print("Division :", quotient)

#10
k = 25
l = 4
floor_division = k//l
print("Division Floored value :", floor_division)

#11
m = 47
n = 5
remainder = m % n
print("Remainder :", remainder)

#12
var1 = 8
var2 = 2
square = var1**var2
print("Value of first variable to the power of second variable :", square)

#Pattern Assignment Questions 

#1 Print a square hollow pattern
print("*"*6) 
print(("*"+" "*4+"*\n")*4, end="")
print("*"*6)

#2 Print a Square Fill Pattern
print(("*"*7+"\n")*7, end="")

#3 Print a hollow rectangle 
print("#"*6)
print(("#"+" "*4+"#\n")*3, end="")
print("#"*6)

#4 Print a filled Square
print(("#"*8+"\n")*6, end="")

#5 Print a Number Triangle Pattern
print(("1\n"+"22\n"+"3"*3+"\n"+"4"*4+"\n"+"5"*5+"\n"+"6"*6))

#5 with loop method
for i in range(1, 7):
    print(str(i)*i)

#6 Up pointing arrow
print(" "*4+"*"+" "*4)
print(" "*3+"*"+" "+"*"+" "*3)
print(" "*2+"*"+" "*3+"*"+" "*2)
print(" "+"*"+" "*5+"*"+" ")
print("*"*3+" "*3+"*"*3)
print((" "*2+"*"+" "*3+"*"+" "*2+"\n")*2, end="")
print(" "*2+"*"*5+" "*2)
