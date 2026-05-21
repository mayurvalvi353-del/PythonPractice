#Normal Method
list = []
for i in range(8):
    list.append("WHITE_PAWN")
print(list)

#List Comprehension Method
list = ["WHITE_PAWN" for i in range(8)]
print(list)

#Squares of numbers
squared_numbers = [index ** 2 for index in range(1, 11)]
print(squared_numbers)

#2 to the power of index
twos = [2**index for index in range(11)]
print(twos)

#Odds from squares 
odds = [x for x in squared_numbers if x % 2 != 0]
print(odds)

