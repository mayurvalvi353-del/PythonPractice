#Bubble sort
list = [8, 10, 6, 2, 4]
swapped = True
count = 0
index = 0
while swapped:
    swapped = False
    for i in range(len(list)-1-index):
        index = i
        count += 1
        if list[i] > list[i+1]:
            swapped = True
            list[i], list[i+1] = list[i+1], list[i]

print(list)
print(count)

#Another method to sort
list.sort()
print(list)