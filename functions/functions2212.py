"""
1. def is a keyword used to define a function

"""

# definintion
def sample():
    print("hi there")

sample()

def sum():
    a=10
    b=20
    return a+b

print("the sum is",sum())

def mul():
    a=10
    b=20
    # return a*b
# when not returned it will return "none"

print("the product is",mul())


# #calculator
# def sum(a,b):
#     return a+b
# def mul(a,b):
#     return a*b
# def sub(a,b):
#     return a-b
# def div(a,b):
#     return a/b
#
# print("enter elements")
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("which operation do you want to perform?")
# print("1.ADDITION\n2.SUBSTRACTION \n3.MULTIPLICATION\n4.DIVISION")
# ch = str(input("Enter choice(1/2/3/4): "))
# if ch=="1":
#     print(a,"+",b,"=" ,sum(a, b))
# elif ch=="2":
#     print(a,"-",b,"=" ,sub(a, b))
# elif ch=="3":
#     print(a,"*",b,"=" ,mul(a, b))
# elif ch=="4":
#     print(a,"/",b,"=" ,div(a, b))
# else:
#     print("INCORRECT INPUT")

####################### TYPES OF ARGUMENTS #############################################3

#DEFAULT ARGUMENTS

# function with 2 keyword arguments grade and school
def student(name, age, grade="Five", school="ABC School"):
    print('Student Details:', name, age, grade, school)

student('Kelly', 12, 'Six')
student('Jessa', 12, 'Seven', 'XYZ School')

# KEYWORD ARGUMENT

# function with 2 keyword arguments
def student(name, age):
    print('Student Details:', name, age)

student('Jessa', 14)
student( age=12, name='Jon')
student('Donald', age=13)

#ARBITARY ARGUMENTS

def percentage(*args):
    sum = 0
    for i in args:
        # get total
        sum = sum + i
    # calculate average
    avg = sum / len(args)
    print('Average =', avg)

percentage(56, 61, 73)

#KEYWORD ARBITARY ARGUMENTS

def percentag(**kwargs):
    sum = 0
    for sub in kwargs:
        # get argument name
        sub_name = sub
        # get argument value
        sub_marks = kwargs[sub]
        print(sub_name, "=", sub_marks)

# pass multiple keyword arguments
percentag(math=56, english=61, science=73)

"""
1.write a python function to find the max of three numbers
2. write a python function to sum all the numbers in a list
3. write a python function to multiply all the numbers in a list

"""

# 1.write a python function to find the max of three numbers

# def max1(a):
#     for i in range(0,len(a)):
#         max=a[0]
#         if a[i]<a[i+1]:
#             max=a[i+1]
#     return max
#
# list2=[1,2,3]
# print("THE MAX IS" ,max1(list2))

# 2. write a python function to sum all the numbers in a list

def sumlist(list1):
   sum=0
   for i in list1:
       sum=sum+i
   return sum
"""

1.	Multiply all the numbers in a list using function 
2.Write a Python program to reverse a string.
Sample String: "1234abcd"
Expected Output: "dcba4321"
3	Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
4. Write a Python function that takes a number as a parameter and check  the number is prime or not.
5. Create an inner function to calculate the addition in the following way
•	Create an outer function that will accept two parameters, a and b
•	Create an inner function inside an outer function that will calculate the addition of a and b
•	At last, an outer function will add 5 into addition and return it
6. Generate a Python list of all the even numbers between 4 to 30
Expected o/p:
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
 Hint:
•	Use the built-in function range() to generate the sequence of numbers between the given start number to the stop number with a step = 2 to get even numbers.
•	pass range() function to a list constructor to create a list



"""
# 1. write a python function to multiply all the numbers in a list
list1=[1,2,3,4,5]
# print("SUM IS",sumlist(list1))
# print("SUM IS",sumlist(list1=[1,2,3]))
#
# def prolist(list1):
#    pro=1
#    for i in list1:
#        pro=pro*i
#    return pro
#
# print("PRODUCT IS",prolist(list1))
# print("PRODUCT IS",prolist([1,2,3]))

# 2.Write a Python program to reverse a string.

# def revlist(str1):
#     return str1[::-1]
#
# str1="123abc"
# print("Reverse is:",revlist(str1))

# 3. Write a Python function to calculate the factorial of a number (a non-negative
# integer).The function accepts the number as an argument.
# def fact(num):
#     f=1
#     if num ==1:
#         return 1
#     else:
#         f=num*fact(num-1)
#     return f
#
# num=int(input("Enter the number : "))
# print("Factorial of", num, "is",fact(num) )

# 4. Write a Python function that takes a number as a parameter and check
# the number is prime or not
#
# def prime(num):
#     flag=0
#     if num==1 or num==0:
#         flag=1
#     else:
#         for i in range(2,int(num/2)):
#             if num%i==0:
#                 flag=1
#                 break
#     if flag==1:
#         return 1
#     else:
#         return 0
#
# num=int(input("Enter a number "))
# f=prime(num)
# if f==1:
#  print(num,"is not a prime number")
# else:
#  print(num, "is a prime number")

# 5

# def outer(a,b):
#
#    def inner(a,b):
#       return a+b
#
#    c = inner(a, b)
#    return c+5
#
# a=int(input("Enter the first digit : "))
# b=int(input("Enter the second digit : "))
# print("Sum is ",outer(a,b))

# 6.
# def evenlist(start,end):
#  list2=[]
#  for i in range(start,end,2):
#     list2.append(i)
#  return list2
#
# start=int(input("Enter the Starting digit: "))
# end=int(input("Enter the limit: "))
# print("The list is",evenlist(start,end))
#

