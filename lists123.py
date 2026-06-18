numbers = [10, 5, 7, 2, 1]
print(numbers)
print(type(numbers))

print("first element content :", numbers[0])
print("second element content :", numbers[1])
print("third element content :", numbers[2])
print("fourth element content :", numbers[3])
print("fifth element content :", numbers[4])

numbers[0] = 111
print("numbers[0]:", numbers[0])
print(numbers)

numbers[1] = numbers[4]
print(numbers)

print(len(numbers))
del numbers[3]
print(numbers)
print(len(numbers))

print(numbers[-1])
print(numbers[-2])
print(numbers[-3])
print(numbers[-4])
print(numbers[-5])
print(numbers[4])

hat = [1, 2, 3, 4, 5]
print(len(hat))
print(hat)
del(hat[4])
print(hat)
i = int(input("Enter the number :"))
hat[int(len(hat)//2)] = i

print(hat)

list = [5,4,3,2,1]
print(list)
list.append(6)
print(list)

list.insert(0, 10)
print(list)