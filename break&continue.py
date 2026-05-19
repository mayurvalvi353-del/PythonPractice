'''print("The break instructions :")
for counter in range(1,6):
    if counter == 3:
        continue
        #break
    print("Inside the loop.", counter)
print("Outside the loop.")'''

counter = 1
while counter < 5:
    print(counter)
    counter += 1
else:
    print("else:", counter)