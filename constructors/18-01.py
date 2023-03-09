"""
1. it is the memebr function of a class, which will be
automatically executed when object of a class created
2. dont have return value
3. two types of constructor- non parameterized (default constructor)
                           - parameterized
"""
# basic example
class A:
    def __init__(self):
        print("NON PARAMETERIZED CONSTRUCTOR")

ob1=A()

class B:
    def __init__(self,name):
        print("PARAMETERIZED CONSTRUCTOR")
        self.na=name
    def __del__(self):
        print("Destructors")
    def display(self):
        print("Name: ",self.na)

ob2=A("Arun")
del ob2
ob2.dispplay

