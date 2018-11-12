#!/bin/python
"""
Case1: Class Creation. 
Object creation will trigger __init__ which is similar to constructor in CPP.
This initializes the properties defined for the class.
self is the pointer to that instance which will be unique for each object
do_work is the method defined in the class.
"""
class Human:
    def __init__(self,n,o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.name == "Saju":
            print (self.name + " is a " + self.occupation + " attempting to learn OOPs")
        else:
            print (self.name + " is not Saju")

# Case 2: Inheritance. Vehicle is the base class and Car/Bike is inherited class
class Vehicle:
    def __init__(self):
        print ("Vehicle init")

    def general_info(self):
        print ("General is Transportation")


class car(Vehicle):
    def __init__(self):
        print ("I am Car init")
        self.name = "Car"
        self.wheels = "4"

    def specific_use(self):
        print (self.name + " used for Family Trip")
        print (self.name + " has" + self.wheels + " wheels")

class bike(Vehicle):
    def __init__(self):
        print ("I am Bike init")
        self.name = "Bike"
        self.wheels = "2"

    def specific_use(self):
        print (self.name + " used for Road Trip")
        print (self.name + " has" + self.wheels + " wheels")

print ("START")
"""
#Case 1: obj1 and obj2 are 2 different instances to class "Human"
obj1 = Human("Saju","Programer")
obj2 = Human("S1","something")

obj1.do_work()
obj2.do_work()
"""
c = car()
b = bike()

c.general_info()
c.specific_use()

b.general_info()
b.specific_use()

print ("END")
