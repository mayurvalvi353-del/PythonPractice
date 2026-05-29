#Class
class ThisIsMyFirstClass :
    name = "Mayur"
    age = 21

    def getName(self):
        print(self.name)
#Object
firstObject = ThisIsMyFirstClass()
print(firstObject)

firstObject.getName()
print(firstObject.name)

class Student :
    def __init__(self, name, age, gender, grade):
        self.name = name
        self.age = age
        self.gender = gender
        self.grade = grade

    def printDetails(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Gender :", self.gender)
        print("Grade :", self.grade)

mayur = Student("Mayur Valvi", 21, "Male", "4th Year")
print(mayur)

mayur.name = "Mayur Valvi"
mayur.age = 21
mayur.gender = "Male" 
mayur.grade = "4th Year"

print(mayur.name)
print(mayur.age)
print(mayur.gender)
print(mayur.grade)

mayur.printDetails()