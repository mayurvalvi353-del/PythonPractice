def message():                #Defining the function
    print("Enter a value : ")

message()          #Invoking / Calling the function 
a = int(input())

message()
b = int(input())

message()
c = int(input())

def message():
    print("Enter a value : ")

#message = 1
print("We start here")
print(message)
message()
print("We end here")

def message():
    print("Enter a value : ")
    temp = int(input())
    return temp

print("Step 1")
a = message()

print("Step 2")
b = message()

print("Step 3")
c = message()

print("a :", a)
print("b :", b)
print("c :", c)
 
def hello(n) :
    print("Hello,", n)

name = input("Enter your name : ")
hello(name)

def message(number):
    print("Enter a number :", number)

number = 1234
message(1)
print(number)

def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message(11, "telephone")
message("price", 5)
message("number", "number")

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

introduction(first_name= "James", last_name= "Bond")
introduction(last_name= "Skywalker", first_name= "Luke")

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a+b+c)

adding(1,2,3)
adding(c = 1, a = 2, b = 3)
adding(3, c = 1, b = 2)
adding(3, a = 1, b = 2)

def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes :
        return
    print("Happy new Year!")

happy_new_year(False)

def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")

def checkMyVar(variable):
    if(variable == 10):
        print("Variable is 10")
        return 2
    else :
        print("Variable is not up to the mark")
        return
    
checkMyVar(5)
print()

def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s
print(list_sum([5, 4, 3]))

def strange_list_fun(n):
    strange_list = []

    for i in range(0, n):
        #strange_list.insert(0, i+1)
        strange_list.append(i+1)
    return strange_list

print(strange_list_fun(5))
