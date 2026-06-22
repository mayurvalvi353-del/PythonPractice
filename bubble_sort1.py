list = [8, 10, 6, 2, 4]
swapped = True
while swapped :
    swapped = False
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            swapped = True
            list[i], list[i+1] = list[i+1], list[i]

print(list)