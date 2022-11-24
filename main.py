# if __name__ == '__main__':
#     print('Python Core')

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



# Encapsulation
# It describes the idea of wrapping data and the methods that work on data within one unit.

# Protected Members
# Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class
# but can be accessed from within the class and its subclasses.
# To accomplish this in Python, just follow the convention by prefixing the name of the member by
# a single underscore “_”.


class Base:
    def __init__(self):
        # Protected member
        self._a = 2


class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ",
              self._a)

        self._a = 3
        print("Calling modified protected member outside class: ",
              self._a)


obj1 = Derived()

obj2 = Base()

print("Accessing protected member of obj1: ", obj1._a)

print("Accessing protected member of obj2: ", obj2._a)
"""


"""    
# Polymorphism
# Having many forms
# It means the same function name (but different signatures) being used for different types.
# The key difference is the data types and number of arguments used in function.

# Example - 1
print(len("geeks"))
print(len([10, 20, 30]))


def add(x, y, z=0):
    return x + y + z


print(add(2, 3))
print(add(4, 5, 6))

# Polymorphism with class methods


class India:

    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA:

    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
"""
# ------------------------------------------------------
"""
print("Some basic exercises")
print("Program to check a palindrome number - ")
# Exercise - 1

num = int(input("Enter any number : "))
temp = num
rev = 0
while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if temp == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

# Exercise - 2
print("Program to check a palindrome string - ")
str = input("Enter any word - ")
if str == str[::-1]:
    print("The letter is a palindrome")
else:
    print("The letter is not a palindrome")
"""

# ----------------------------------------------------------------------------------

# Syntax error -
# This error is caused by the wrong syntax in the code. It leads to the termination of the program.

# Exceptions -
# Exceptions are raised when the program is syntactically correct, but the code resulted in an error.
# This error does not stop the execution of the program, however, it changes the normal flow of the program.

# Example -
marks = 29
# print(marks/0)
# This will show ZeroDivisionError

# Example -2
a = ('1', '2', '3')
# print(a[3])
# Tuple index out of range

# To handle these errors - try and catch statements are used.
# They used to catch and handle exceptions
# Statements that can raise exceptions are kept inside the try clause
# and the statements that handle the exception are written inside except clause.

"""
print("Enter first number - ")
a = input()
print("Enter second number - ")
b = input()
try:
    print("The sum of 2 numbers is ",
          int(a)+int(b))
except Exception as e:
    print(e)


# There can be multiple exceptions in a program

z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(z)
print("Enter any index number - ")
try:
    b = int(input())
    print("Value at", b, "position is ", (z[b]))
except ValueError:
    print("Value Error - Please enter integer value only")
except Exception as e:
    print(e)


# Try with else clause -
# Use the else clause on the try-except block which must be present after all the except clauses.
# The code enters the else block only if the try clause does not raise an exception.

z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(z)
print("Enter any index number - ")
try:
    b = int(input())
    print("Value at", b, "position is ", (z[b]))
except Exception as e:
    print(e)
else:
    print("Code successfully executed")  # This code will execute only if there is no exceptions raised.

# Finally
# Statements written in finally keyword is always executed after try and except blocks.
# Final block always executes after normal termination of try block or after try block terminates due to some exception.

    # Syntax:
# try:
#      Some Code....
#
# except:
#      optional block
#      Handling of exception (if required)
#
# else:
#      execute if no exception
#
# finally:
#     Some code .....(always executed)

    print("-----------------------------")
# Example -

try:
    k = 5 // 0
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print("Always executed")
"""

# NZEC (non zero exit code) 
# occurs when your code is failed to return 0. When a code 
# returns 0 it means it is successfully executed otherwise it will 
# return some other number depending on the type of error.
# Example -
# n = int(input())
# k = int(input())
# print n," ",k















