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

#Reverse the list
list.reverse()

#Slice
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_1)
print(list_2)

list = [10, 8, 6, 4, 2]
new_list = list[1:3]
print(new_list)

new_list = list[1:-1]
print(new_list)

new_list = list[-5:3]
print(new_list)

new_list = list[:3]
print(new_list)
new_list = list[2:]
print(new_list)

list = [10, 8, 6, 4, 2]
del list[1:3]
print(list)
del list[:]
print(list)

#in & not in
list = [0,3,12,8,2]
print(5 in list)
print(5 not in list)
print(12 in list)