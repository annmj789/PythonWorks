# #string
# #ordered, immutable, quates needed, indexed
#
# #join
#
#
# #string slicing
# str="Ann Mary"
# print(str[2])
# print(str[-2])
# print(str[2:5])
# print(str[2:-1])
# print(str[0:7:-1])#not getting @@@@@@@
# print(str[::3])
# print(str.lower())
# print(str.upper())
# print(str.swapcase())
# str1="AAMM"
# print(str1.islower())
#
#
# #split()
# print(str.split())
# #concatenation
# st1 = "ann"
# st2 = "mary"
# st3 = st1 + " " + st2
# print(st3)
#
# # length
# print(len(st3))
#
#
# # find()
# print(str.find("na"))
# print(str.find("z"))
#
#
# # replace()
# str1 = "ann mary"
# print(str1.replace("ann", "rose"))
# print(str1.replace("n", "m", 2))
# str[0] = "t"


# #string formatting
# name="ann"
# age=23
# print("%s is %d years old"% (name,age))
# print("{} is {} years old".format(name,age))
# print(f'{name} is {age} years old')
#
# bag=3
# apples=10
# print(f'{apples*bag} apples are there')
#

#############################   ASSIGNMENT   ###################################
#1. remove empty strings from a list of strings
str1=["John","","Jack","Emma","","jins","lina"]
print(str1)
i=0
while i<len(str1):
    if len(str1[i]) == 0:
        str1.pop(i)
    i=i+1
print(str1)

#2.
str3="Lets google the pineapple"
str4=str3.split(" ")
str5=[]

for i in str4:
    l=""
    for j in i:
        if j in l:
            continue
        else:
            l=l+j
    str5.append(l)
    print(str5)
print(" ".join(str5))

list1=["a","b "]
print(" ".join(list1))


#3 replace every special character with #
str2="@im $ann (mary"
str2=str2.replace("@","#").replace("$","#").replace("(","#")
print(str2)

"""
WAP to get a string from a string where all occurances of its 
first char have been changed to $, except the first char itself
eg: restart
op: resta$t
"""
str6="restart"
str7=str6[0]
for i in range(1,len(str6)):
    print(str6[i])
    if str6[i] == str6[0]:
        str7=str7+"$"
    else:
        str7=str7+str6[i]
print(str7)





