blocks = int(input("Enter the number of Blocks : "))

height = 0
used_blocks = 0
layer = 1

while used_blocks + layer <= blocks :
    used_blocks += layer
    height += 1
    layer += 1

print("The height of the pyramid :", height)