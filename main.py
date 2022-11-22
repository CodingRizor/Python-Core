# if __name__ == '__main__':
#     print('Python Core')
# ---------------------21-11-22-----------------------
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

"""
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
"""
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
"""

# -----------------------22-11-22-----------------------------
# Class-----
"""
class Computer:
    def __init__(self, cpu, ram, hdd, ssd):
        print("Init called")
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
        self.ssd = ssd

    def config(self):
        print("Config is", self.cpu, self.ram, self.hdd, self.ssd)
# print('i5, 16Gb RAM, 1 Tb hard-disk, 256 Gb SSD')


# com1 = Computer() without init
com1 = Computer('i5', '16Gb RAM', '2 Tb hard-disk', "1 Tb ssd")
print(type(com1))
# Computer.config(com1)  # Another method
com1.config()
"""

# Constructors-

"""
class Data:
    def __init__(self):
        self.name = "Dhairya"
        self.age = 21

    def update(self):
        self.age = self.age + 1
        return self.age

    def compare(self, other):
        if self.age == other.age:
            print("True")
        else:
            print("False")


c1 = Data()  # Constructor allocates size of an object
c2 = Data()
print("Address of c1 -", id(c1))
print("Name -", c1.name, ", Age -", c1.age)
print("Age after one year", c1.update())

c2.name = "Divyansh"
c2.age = 22
print("Address of c2 -", id(c2))
print("Name -", c2.name, ", Age -", c2.age)
print("Age after one year", c2.update())
# print(c1.age == c2.age)  # Comparing two objects
c1.compare(c2)
"""

# Types of Variables -
# 1. Class Variable - Declared outside the init --- Same for every object
# 2. Instance Variable - Declared inside the init --- Changes according to the instance

"""
class Car:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.company = "BMW"


c1 = Car()
c2 = Car()
print(c1.company, c1.mil, c1.wheels)
print(c2.company, c2.mil, c2.wheels)
"""

# Types of methods
# 1. Instance method - works upon instance variables
# 2. Class methods -  works upon class variables
# @classmethod
# 3. Static method - don't need to use any variable
# @staticmethod

"""
class Marks:
    school = "Rajasthan University"

    def __init__(self, m1, m2, m3):   # Instance method
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        print("Marks -", m1, m2, m3)

    def average(self):    # Instance method
        print((self.m1+self.m2+self.m3)/3)

    # def info(cls):       # Class method
    #     print(cls.school)
    @classmethod
    def info(cls):       # Class method (Decorator)
        print(cls.school)

    @staticmethod
    def data():
        print("All the best")


s1 = Marks(78, 89, 83)
s2 = Marks(79, 82, 89)
s1.average()
s2.average()
s1.info()
s2.info()
# Marks.info(cls=Marks)
Marks.info()
# Accessors - get the values only (getters)
# Mutators - set the values (setters)
Marks.data()  # Can be accessed by class or objects
s1.data()
s2.data()
"""

# Nested Class
# Class inside a class(inner class)

"""
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.Lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.model = "272tx"

        def show(self):
            print(self.brand, self.model)


s1 = Student('Dhairya', '01')
s2 = Student("Divyansh", '02')
s1.show()
s2.show()
print(id(s1.Lap.brand), id(s1.Lap.model))  # Accessing nested class data
s1.Lap.show()
"""


# Inheritance
# It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and
# methods by deriving a class from another class.
# Inheritance is the capability of one class to derive or inherit the properties from another class.


class A:

    def feature1(self):
        print("Feature 1")

    def feature2(self):
        print("Feature 2")


class B(A):  # SINGLE LEVEL INHERITANCE - CLASS B ACQUIRES PROPERTIES OF CLASS A ONLY

    def feature3(self):
        print("Feature 3")

    def feature4(self):
        print("Feature 4")


class C(B):  # MULTI-LEVEL INHERITANCE -  CLASS C ACQUIRES PROPERTIES OF BOTH CLASS B AS WELL AS C

    def feature5(self):
        print("Feature 5")


class D:

    def feature6(self):
        print("Feature 6")


class E(A, D):  # MULTIPLE INHERITANCE - CLASS D ACQUIRES PROPERTIES OF ONLY CLASS A AND D

    def feature7(self):
        print("Feature 7")


a1 = A()
a1.feature1()
a1.feature2()
print("---------")
b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
print("---------")
c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
print("---------")
e1 = E()
e1.feature1()
e1.feature2()
e1.feature6()
e1.feature7()


# Private Members of the parent class
# Make an instance variable private by adding double underscores before its name.
# To stop instance variables of the parent class to be inherited by the child class, variable is made private.


class A1:
    def __init__(self):
        self.num = 21

        self.__num1 = 29


class B1(A1):
    def __init__(self):
        self.num2 = 8
        A1.__init__(self)


obj1 = B1()
# print(obj1.num1)  # Error will show as num1 is private instance variable
print("----------")
print(obj1.num)
print("----------")


# Hierarchical Inheritance
# When more than one derived class are created from a single base class.

# Base class
class Parent:
    def func1(self):
        print("Parent Class function")


class Child1(Parent):
    def func2(self):
        print("Child1 Class Function")


class Child2(Parent):
    def func3(self):
        print("Child2 Class Function")


object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
print("----------")
object2.func1()
object2.func3()


# Hybrid Inheritance
# Inheritance consisting of multiple types of inheritance is called hybrid inheritance.

class Info:
    def funcinfo(self):
        print("This function is in Class Info")


class Data(Info):
    def funcdata(self):
        print("This function is in class Data")


class Record(Info):
    def funrecord(self):
        print("This function is in class Record")


class Statistics(Data, Info):
    def funstatistics(self):
        print("This function is in class statistics")


print("----------")
object3 = Statistics()
object3.funcinfo()
object3.funstatistics()
object3.funcdata()
