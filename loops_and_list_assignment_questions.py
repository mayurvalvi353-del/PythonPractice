#1. First 10 Natural numbers
for i in range(1,11):
    print(i)

#2. Even numbers within the range of 10
for i in range(1,11):
    if i % 2 == 0 :
        print(i)

#3. Sum of all numbers
n = 15
total = 0 
for i in range(1,n+1):
    total += i
print(total)

#4. Sum of all odd numbers
n = 15
total = 0
for i in range(1, n+1):
    if i % 2 != 0 :
        total += i
print(total)

#5. Multiplication table of a given number 15
m = 15
for t in range(1, 11):
    print(m,"x",t,"=",m*i)

#6. Display numbers from a list using a for the loop
list = [1, 2, 4, 6, 88, 125]
for a in list :
    print(a)

#7. Count the total number of digits in a number
number = 129475
count = 0
while number != 0:
    number = number // 10
    count += 1
print(count)

#8. ⁠Check if the given string is a palindrome
string = "madam"

if string == string[::-1]:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")

#9. Program that accepts a word from the user and reverses it
word = input("Enter the word : ")
rev_word = ""

for i in word :
    rev_word = i + rev_word

print(rev_word)

#10. Program to check if a given number is an Armstrong number 
num = 153
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

#Program to count the number of repeated characters and unique characters in a string
string = "UraanSoftskills"

repeated = 0
unique = 0
checked = ""

for ch in string:
    if ch not in checked:
        count = 0

        for c in string:
            if c == ch:
                count += 1

        if count > 1:
            repeated += 1
        else:
            unique += 1

        checked += ch

print("Repeated characters:", repeated)
print("Unique characters:", unique)

#Find frequency of each character
string = "UraanSoftskills"
checked = ""

for ch in string:
    if ch not in checked:
        count = 0

        for c in string:
            if c == ch:
                count += 1

        print(ch, ":", count)
        checked += ch

#Vowel Eater
user_word = input("Enter a word: ")
user_word = user_word.upper()

word_without_vowels = ""

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels)

#Program to print numbers from 1 to 50 in this pattern : [1, 2, Fiz, 4, Buzz, Fiz, 7, 8, Fiz, Buzz, 11, Fiz, 13, 14, FizBuzz, 16....50]
for i in range(1, 51):
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

#Program to count number of digits
string = "MindCoders password2 is : 1234"

count = 0

for ch in string:
    if ch.isdigit():
        count += 1

print("Total number of Digits =", count)

string2 = "U r a a n S 0 f t s k i l l 1 s 1234"

count1 = 0

for ch in string2:
    if ch.isdigit():
        count1 += 1

print("Total number of Digits =", count)

#Program to Count Occurrence of 's' or 'S'
string = "MindCoders"

count = 0

for ch in string:
    if ch == 's' or ch == 'S':
        count += 1

print("Count =", count)

#Beatles 
beatles = []
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
#print(beatles)
for i in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(i)
#print(beatles)
del(beatles[3])
del(beatles[3])
#print(beatles)
beatles.insert(0, "Ringo Starr")
print(beatles)

#Hat problem
hat_list = [1, 2, 3, 4, 5]

print(len(hat_list))

del hat_list[4]

hat_list[len(hat_list) // 2] = int(input("Enter a number: "))

print(hat_list)

