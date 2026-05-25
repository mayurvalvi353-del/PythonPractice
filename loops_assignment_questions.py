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
text = input("Enter the word : ")
it_is = True

for i in range(len(text) // 2):
    if text[i] != text[-(i+1)]:
        it_is = False
        break

if it_is :
    print("Palindrome")
else :
    print("Not Palidrome")

#9. Program that accepts a word from the user and reverses it
word = input("Enter the word : ")
rev_word = ""

for i in word :
    rev_word = i + rev_word

print(rev_word)

#10. Program to check if a given number is an Armstrong number 
