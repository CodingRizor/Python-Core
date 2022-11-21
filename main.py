if __name__ == '__main__':
    print('Python Core')

# Class
# A class is a user-defined blueprint or prototype from which objects are created.
# Classes provide a means of bundling data and functionality together.
"""
Syntax -
class ClassName:
       ----------
       Statements
       ----------
"""


# Class creates a user-defined data structure, which holds its own data members and member functions,
# which can be accessed and used by creating an instance of that class.
# Attributes are always public and can be accessed using the dot (.) operator.
# Eg.: Class.attribute

# Objects
# An Object is an instance of a Class.
# A class is like a blueprint while an instance is a copy of the class with actual values.
# State - It is represented by the attributes of an object. It also reflects the properties of an object.
# Behaviour - It is represented by the methods of an object.
# Identity - It gives a unique name to an object and enables one object to interact with other objects.
# When an object of a class is created, the class is said to be instantiated.


class Dog:
    color = "Black"
    age = 10

    def fun(self):
        print("--", self.color)
        print("--", self.age)


Bronnie = Dog()  # Creating Objects
Fluffy = Dog()
print(Bronnie, Fluffy)  # Object created at different location
print(Bronnie.color)
print(Bronnie.age)
# Second way - calling bu function
Bronnie.fun()


# Example - 2
class Student:
    pass


s1 = Student()
s2 = Student()
s1.name = "Dhairya"
s1.age = 21
s1.hobbies = ['Gaming', 'Coding', 'Watching Series']
s2.name = "Divyansh"
s2.age = 22
print(s1.name)
print(s1.__class__)  # getting class
print(s1.hobbies)


# Instance and class variables
class Employee:
    pl = 12

    def __init__(self, aname, asalary, apost):  # Constructor - called when object is created
        self.name = aname
        self.salary = asalary
        self.post = apost

    def printdetails(self):  # a method for printing data members
        return f"Name - {self.name}, Salary - {self.salary} Post - {self.post}"

    @classmethod
    def changepl(cls, newpl):
        cls.pl = newpl

    @classmethod  # class method as alternative constructors
    def fromslash(cls, string):
        return cls(*string.split("/"))


d1 = Employee('', '', '')  # creating Object
a1 = Employee('', '', '')
c1 = Employee("Divyansh", 10000, "Intern")
d1.name = "Dhairya"
d1.salary = 10000  # Instance variable
d1.post = "Intern"
a1.name = "Ashish"
a1.salary = 10000
a1.post = "Junior Developer"
print(d1.__dict__)
print(Employee.pl)
Employee.pl = 15
print(d1.pl)
print(d1.__dict__)
# If we change class variables by object d1 then -
d1.pl = 14
print(d1.__dict__)
print(Employee.__dict__)
print(d1.printdetails())  # calling instance method
print(a1.printdetails())
print(c1.__dict__)
print(c1.printdetails())
Employee.changepl(20)  # this will work as normal
print("Changed by Employee class -", Employee.pl)
# To change a class variable by a method using an instance
d1.changepl(16)
print("Changed by object -", Employee.pl)
k1 = Employee.fromslash("Kartik/10000/Intern")
print(k1.__dict__)


# Static Method - Normal methods without class and instance variables
# Static method is bound to a class rather than the objects for that class.
# Syntax-
# @staticmethod
# def ------():
#      Statements
class StaticClass:
    @staticmethod
    def info(string):
        print("Welcome " + string)
        return "********"


data1 = StaticClass()
print("--------")
print(data1.info("Dhairya"))

del data1  # deleting an object
# print(data1.info("Dhairya")) - Show error not defined

# Destructors-
# Destructors are called when an object gets destroyed
# The __del__() method is a known as a destructor method in Python.
# It is called when all references to the object have been deleted i.e when an object is garbage collected.
# Syntax-
# def __del__(self):
#   body of destructor

"""

class Employee:

    # Initializing
    def __init__(self):
        print("----------------------------------")
        print('Employee created.')

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called')
        print('Employee deleted')
        print("----------------------------------")


obj = Employee()

"""


# Another example to understand the full working of destructor

class Des:
    def __init__(self):
        print("Employee Created")

    def __del__(self):
        print("Destructor Called")


def crobj():
    print("Creating Object")
    f1 = Des()
    print("Function End")
    return f1


print("Calling crobj function")
f1 = crobj()
print("Program End")
    