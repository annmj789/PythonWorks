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
