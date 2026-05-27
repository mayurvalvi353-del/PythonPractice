dictionary = {
"cat" : "chat",
"dog" : "chien",
"horse" : "cheval"
}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

print(dictionary)
print(type(dictionary))
print(phone_numbers)
print(type(phone_numbers))
print(empty_dictionary)
print(type(empty_dictionary))

print(dictionary["cat"])
print(phone_numbers["Suzy"])

words = ['cat', 'lion', 'horse']

for word in words :
    if word in dictionary :
        print(word, "->", dictionary[word])
    else :
        print(word,"is not in dictionary")

print(dictionary.keys())

for key in dictionary.keys():
    print(key,"->",dictionary[key])

for key, value in dictionary.items():
    print(key,"->",value)

print(dictionary.items())

for value in dictionary.values():
    print(value)

pol_eng_dictionary = {
 "zamek": "castle",
 "woda": "water",
 "gleba": "soil"
 }
print("pol_eng_dictionary :", pol_eng_dictionary)
copy_dictionary = pol_eng_dictionary.copy()

print("copy_dictionary :", copy_dictionary)

pol_eng_dictionary["zamek"] = "lock"
item = pol_eng_dictionary["zamek"]
print(item)

phonebook = {}

phonebook["Adam"] = 3456782996
phonebook["Lily"] = 6547578744
print(phonebook)

del phonebook["Adam"]
print(phonebook)

pol_eng_dictionary = {"kwiat": "flower"}

pol_eng_dictionary.update({"gleba" : "soil"})
print(pol_eng_dictionary)

pol_eng_dictionary.popitem()
print(pol_eng_dictionary)
