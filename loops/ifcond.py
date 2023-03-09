# # Python program to check if year is a leap year or not
#
# year = int(input("Enter the year:"))
#
# if (year % 400 == 0) and (year % 100 == 0):
#     print("{0} is a leap year".format(year))
#
# elif (year % 4 ==0) and (year % 100 != 0):
#     print("{0} is a leap year".format(year))
#
# else:
#     print("{0} is not a leap year".format(year))
########################################################################################
# # VOWEL AND CONSONANT
# charc=input("Enter string  ")
# list=["a","e","i","o","u","A","E","I","O","U"]
# for i in charc:
#    if i in list:
#       print(f"{i} is vowel")
#    else:
#       print(f"{i} is consonant")

#############################################################################################
# ARMSTRONG

num=int(input("enter number"))
sum=0
tmp=num
while tmp>0:
  cube=tmp%10
  sum=sum+(cube*cube*cube)
  tmp=tmp//10
if sum==num:
    print(f"{num}  is an armstrong number")
else:
    print("Not a armstrong number ")

