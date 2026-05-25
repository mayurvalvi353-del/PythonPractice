#Count the number of Unique and Repeated characters

word = input("Enter the word : ")
word = word.upper()
word_without_vowels = ""
for letter in word :
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

    word_without_vowels += letter

print(word_without_vowels)

