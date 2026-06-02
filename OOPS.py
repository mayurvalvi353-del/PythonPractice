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

class ExampleClass :
    def __init__(self, val = 1):
        self.first = val
    
    def set_second(self, val):
        self.second = val

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_2.set_second(3)
example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1)

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

class Classy :
    def method(self, par):
        print("method", par)

obj = Classy()
obj.method(1)

class Classy :
    varia = 2
    def method(self):
        print(self.varia, self.var)

obj = Classy()
obj.var = 3

class Star :
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' is in ' + self.galaxy

sun = Star("Sun", "Milky Way")
print(sun)

#Inheritance Example
class Vehicle :
    pass

class LandVehicle(Vehicle) :
    pass

class TrackedVehicle(LandVehicle):
    pass

for cls1 in [Vehicle, LandVehicle, TrackedVehicle] :
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle] :
        print(issubclass(cls1, cls2), end = "\t")
    print()

class Super :
    def __init__(self):
        self.supVar = 14

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 18

obj = Sub()
print(obj.subVar)
print(obj.supVar)

#Multi-Level Inheritance
class Level1 :
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101
    def fun_1(self):
        return 102
    
class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    def fun_2(self):
        return 202
    
class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301
    def fun_3(self):
        return 302
    
obj = Level3()
print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())
