my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for iterator in range(len(my_list)):
    print(my_list[iterator])

#Updating a list in loop
list = []
for iterator in range(1, 11):
    list.append(iterator)
print(list)

list = []
for iterator in range(10):
    list.append(iterator+1)
print(list)

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for iterator in range(len(my_list)):
     my_list[iterator] += 1

print(my_list)

list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sum = 0
for index in range(len(list)):
     sum += list[index]

print(sum)

list = [10, 1, 8, 3, 5]
total = 0

for element in list :
    total += element
print(total)

#copying variables or swapping variables

var1 = 10
var2 = 20
print("Variable 1 :", var1)
print("Variable 2 :", var2)
var1, var2 = var2, var1
print("Variable 1 :", var1)
print("Variable 2 :", var2)

list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(list)
list[4], list[1] = list[1], list[4]
print(list)

