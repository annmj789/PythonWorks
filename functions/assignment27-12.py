"""
1. WAP funtion to creat and print a list where the values are squares of numbers from 1 to 30
2. Assign a different name to function and call it through the new name
3. Genertae a python list of all even numbers between 2 numbers
4. Python function that accepts two numbers as arguments and returns the sum
5. Python function that accepts different values as parameters and returns a list
6. Python function that accepts different values as parameters and returns a tuple
7. define a function that accepts 2 values and returns its sum, subtraction and multiplication
8. define a function that counts vowels and constants in a word
9. WAP function to check whether its odd or even
"""
#1. WAP funtion to creat and print a list where the values are squares of numbers from 1 to 30

# def sqlist(a,b):
#     list3=[]
#     for i in range(a,b+1,1):
#         list3.append(i**2)
#     return list3
#
# a=int(input("Enter the first digit : "))
# b=int(input("Enter the second digit : "))
# print("List of squares is",sqlist(a,b))

# 2. Assign a different name to function and call it through the new name
# def oldname():
#     print("hey there")
#
# newname=oldname
# newname()
#
# # 3. Genertae a python list of all even numbers between 2 numbers
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
# # 5. Python function that accepts two numbers as arguments and returns the sum
# def sum(a,b):
#     return a+b
#
# a=int(input("Enter the first digit : "))
# b=int(input("Enter the second digit : "))
# print("the sum is",sum(a,b))
#
# #5. Python function that accepts different values as parameters and returns a list
#
# def list1(a,b,c):
#     l=[a,b,c]
#     return l
# a=int(input("Enter the first digit : "))
# b=int(input("Enter the second digit : "))
# c=int(input("Enter the first digit : "))
#
# print(list1(a,b,c))
#
# #6. Python function that accepts different values as parameters and returns a tuple
#
# def tuple1(a,b,c):
#     t=(a,b,c)
#     return t
# a=int(input("Enter the first digit : "))
# b=int(input("Enter the second digit : "))
# c=int(input("Enter the first digit : "))
#
# print(tuple1(a,b,c))
#
# # 7. define a function that accepts 2 values and returns its sum, subtraction and multiplication
#
# def calc(a,b):
#     print(a,"+",b,"=",a+b)
#     print(a,"-", b, "=", a - b)
#     print(a, "*", b, "=", a * b)
#
# a=int(input("Enter the first digit : "))
# b=int(input("Enter the second digit : "))
# calc(a,b)

# 8. define a function that counts vowels and constants in a word

# def vow_cons(str1):
#     str1=str1.lower()
#     v=0
#     c=0
#     for i in range(0,len(str1)):
#         if str1[i] in ["a","i","o","u","e"]:
#             v=v+1
#         elif str1[i] ==" ":
#             continue
#         else:
#             c=c+1
#
#     print("No. of constants ",c)
#     print("No. of vowels is ",v)
#
# str1=str(input("Enter any string : "))
# vow_cons(str1)

# WAP function to check whether its odd or even

# def oddeven(num):
#     if num%2==0:
#         return 0
#     else:
#         return 1
#
# num=int(input("Enter the digit to check : "))
# d=oddeven(num)
# if d==0:
#     print(num,"is even")
# else:
#     print(num,"is odd")