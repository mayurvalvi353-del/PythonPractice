board = []
for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)
#print(board)
for index in board:
    print(index)
print(len(board))

board[0][0] = "ROOKS"
board[0][7] = "ROOKS"
board[7][0] = "ROOKS"
board[7][7] = "ROOKS"

print("-----------------------------")

for index in board:
    print(index)

board[0][1] = "KNIGHT"
board[0][6] = "KNIGHT"
board[7][1] = "KNIGHT"
board[7][6] = "KNIGHT" 

print("-----------------------------")

for index in board:
    print(index)

#Multi-Dimensional List
temps = [[0.0 for h in range(24)] for d in range(31)]

temp1 = 19
temp2 = 32
count = 0

for days in temps:
    if count == 0 :
        days[11] = temp1
        count = 1
    else :
        days[11] = temp2
        count = 0
for element in temps:
    print(element)
 
total = 0.0
for days in temps:
    total += days[11]
average = total / 31
print("Average temperature at noon :", average)

highest = -100.0
for day in temps :
    for temp in day:
        if temp > highest:
         highest = temp
print("The Highest temperature was", highest)

hot_days = 0
for day in temps:
    if day[11] > 20.0 :
        hot_days += 1
print(hot_days, "days were hot days in the month.")

#Three-Dimensional list
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
print(rooms)

rooms[1][9][13] = True
rooms[1][9][1] = True

vacancy = 0
for room_number in range(20):
    if not rooms[1][9][room_number]:
        vacancy += 1
print("Vacancy in 10th floor of 2nd building :", vacancy)

