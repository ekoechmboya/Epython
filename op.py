# classes and objects
#OBJECT ORIENTED PROGRAMMING WE SHOULD TREAT OUR PORGRAMS WITH A LEVEL OF ABSTRACTION AND REUSABILITY
# Class: blueprint for an object: template for creating objects
class TestClass:
    x = 10 #variables in classes are reffered to as properties
    def powerMethod(self):
        y = pow(10, 2)
        print(y)

    #objects are creation of classes

# to create objects reference the class name as a function call
object1= TestClass()
print(object1.x)
print(object1.powerMethod())


# the init() function: initializattion function that definies info about an object created from the blueprint
# self points to the current object being created
class Student:
    def __init__(self, name, age, unit, doa):
        self.name = name
        self.age = age
        self.unit = unit
        self.doa = doa

    def greetstudent(self):
        print("hello " + self.name)


student1 = Student("Joseph", "14", "Form 1", "Thursday")
student2 = Student("Mary", "14", "Form 1", "Thursday")



print(student1.name)
print(student1.greetstudent())
print(student2.greetstudent())

# classes define the property and methods that work on that property

