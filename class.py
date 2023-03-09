# class emp:
#     def fact(sl,x):
#         if x == 1:
#             return 1
#         else:
#             return x*sl.fact(x-1)
#
# obj = emp()
# n = int(input("Enter the number: "))
# f = obj.fact(n)
# print("Factorial is: f")

"""
OPP Concepts
1. Encapsulation-defintion
2. Inheritance-definition, types,
3. Polymorphism- definition, types-run time(Overloading) and compile time(Overriding)
   in python polymorphism doesnt work directly
4. Abstraction- defintion, Abstract class
"""

#inheritance

# class A:
#     def displayA(self):
#         print('Base')
# class B(A):
#     def displayB(self):
#         print("Derive")
# class C:
#     def displayC(self):
#         print("class C")
#
# ob=B()
# ob.displayB()
# ob.displayA()
# # ob.displayC() #Creates error as object of B cannot access C
# ob2=C()
# ob2.displayC()

#sum
# class R:
#     def read(self):
#         self.a=int(input("Enter first number: "))
#         self.b = int(input("Enter second number: "))
#         # sum(a,b)
# class S(R):
#     def sum(self):
#         return self.a+self.b
# class A(S):

#     def avg(self):
#         return (self.a+self.b)/2
# ob=A()
# ob.read()
# print("SUM: ",ob.sum())
# print("AVERAGE",ob.avg())



# class P:
#     def personal(self):
#         self.name=str(input("Enter your name: "))
#         self.age = int(input("Enter your age: "))
# class ED():
#     def empD(self):
#         self.desig = str(input("Enter your designation: "))
#         self.salary = int(input("Enter your salary: "))
# class D(P,ED):
#     def dispaly(self):
#         print("EMPLOYEE DETAILS")
#         print("Name: ", self.name)
#         print("Age: ", self.age)
#         print("Designation: ", self.desig)
#         print("Salary: ", self.salary)
#
# ob3=D()
# ob3.personal()
# ob3.empD()
# ob3.dispaly()


#polymorphism
# class one():
#     def fn(self):
#         print("A")
#
#     def fn(self,x):
#         print(x)
#
#     def fn(self,x,y): # only lastest funtion will be considered
#         print(x,y)
# ob4=one()
# # ob4.fn() wont work
# # ob4.fn(2) wont work
# ob4.fn(2,3)


# class poly2():
#     def message(self,name=None):
#         if name is None:
#             print("hello")
#         else:
#             print("hello ",name)
#
# ob5=poly2()
# ob5.message()
# ob5.message("Ann")

#overring

class name1():
    def nm( name):
        print("My name ", name)
class name2(name1):
    def nm(name):
        print("I am ",name)

ob6=name2
ob6.nm("Ann")

#abstract class

from abc import ABC, abstractmethod
# abstract class
class Polygon (ABC):
#abstract method
#abstract method
 def sides (self):
  def display (self):
      print ("non abstract method")

class Triangle(Polygon):
    def sides (self):
            print("Triangle has 3 sides")

t=Triangle()
t.aides()
t.display()