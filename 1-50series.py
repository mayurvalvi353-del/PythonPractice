number = int(input("Enter the number : "))

count = 1
even = 0
odd = 0
while count <= number:
    if count % 2 == 0 :
        even += 1
    else : 
        odd += 1
    count += 1

print("Even = ", even)
print("Odd = ", odd)

