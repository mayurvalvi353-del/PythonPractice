city = 'Bhopal'
print(city[0])
print(city[2])
print(city[-1])
print(city[5])
print(city[-3])
print(city[3])

name = 'Mayur Valvi'

print(name[0:5])
print(name[6:])
print(name[:5])
print(name[::2])
print(name[::-1])

print(len(city))
print(len(name))

text = '  Hello Python World!  '
#Case
print(text.upper()) #converts to uppercase
print(text.lower()) #converts to lowercase
print(text.title()) #Every first letter of the string will be capital 
print(text.capitalize()) #First letter of string can be uppercase or lowercase

#Strip whitespace
print(text.strip()) #Eliminates the unnecessary blank spaces at start and end

#Search
print('Python' in text) #Returs True or False on the basis of existence
print(text.find('Python')) #Returns the starting index of given word
print(text.count('o')) #Returns the frequency of given letter

#Replace
print(text.replace('Python', 'AI')) #Replace first word with second word

#Split and Join
csv = 'Mayur,22,Indore,Engineer'
parts = csv.split(',')  #Splits the sentence from given character
print(parts)
print(parts[0])
rejoined = ' | '.join(parts) #Joins with given character
print(rejoined)

#Check Content
print('hello123'.isalnum()) #Checks is there are any numbers or not
print('12345'.isdigit()) #Checks whether in string all are numbers or not
print('Python'.isalpha()) #Checks whether all are alphabets or not
print('  '.isspace()) #Checks whether there is space in string or not

#Start/End check
email = 'mayur@gmail.com' 
print(email.endswith('.com')) #Checks whether is string ends with given letter
print(email.startswith('may')) #Checks whether is string starts with given letter

#F-string methods
name, marks, rank = 'Mayur', 92.567, 3

print(f'Hello, {name}!')

#Format Numbers
print(f'Marks : {marks:.2f}') #Returns two decimal places
print(f'Marks : {marks:.0f}') #rounded number
print(f'Count : {1000000:,}') #comma seperator

#Padding & Alignment
print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}') #left/right align
print(f'Hello {name:^10}')
print(f'Hello {name:>10}')
print(f'Hello {name:<10}')
print(f'Hello {name:*^11}')

#Expressions inside {}
price, gst = 500, 0.18
print(f'Price : Rs.{price} | GST : Rs.{price*gst:.2f} | Total : Rs.{price*(1+gst):.2f}')

string = "Hello, How are you doing today ?"
#Count Vowels in the string
vowels = 'aeiouAEIOU'
count = 0
for i in string :
    if i in vowels :
        count += 1
print("Vowels count :", count)

#Print you from the string
print(string[15:19])

#Print the string in reverse order
print(string[::-1])

non_palin, palin = 'abcdef', 'axttxa'
#Check if the string is palindrome or not
print("Is non_palin is palindrome :",non_palin == non_palin[::-1])  
print("Is palin is palindrome :",palin == palin[::-1])          




