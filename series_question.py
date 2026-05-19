#1
for i in range(1,51):
    if i == 50 :
        print(i, end="")
    else :
        print(i, end=", ")

#2
for i in range(1,51):
    if i % 2 == 0 and i != 50:
        print("t", end=", ")
    elif i == 50 :
        print(i, end=" ")
    else :
        print(i, end=", ")


#3
for i in range(1, 51):
    if i % 3 == 0 :
        print("t", end=", ")
    elif i == 50 :
        print(i, end=" ")
    else :
        print(i, end=", ")


#4
for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizbuz", end=", ")
    elif  i % 3 == 0 :
        print("fiz", end=", ")
    elif i % 5 == 0 and i != 50 :
        print("buz", end=", ") 
    elif i == 50 :
        print(i, end=" ")
    else :
        print(i, end=", ")

