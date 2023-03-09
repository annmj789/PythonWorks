#findall()- it returns a list contain all matches

import re
str="Rose is a beautiful and colorful flower cul sul  345 6 5434 22234 3343"
# s=re.findall("ful",str)
# print(s)
# t=re.findall("[cs]",str)
# print(t)
# u=re.findall("[cs]ul",str)
# print(u)
# v=re.findall("[^cs]",str)
# print(v)
# w=re.findall("\d{1,3}",str)
# print(w)
# x=re.findall("\d{3}",str)
# print(x)
# x=re.findall("\b\d{3}\b",str)
# print(x)

# Search()- it reaturn a match object if there is a match anywhere in the string
# a=re.search("\s",str)
# print(a)
# print(a.start())
#
# b=re.search("\d",str)
# print(b)
# print(b.start())
#
# c=re.search("ann",str)
# print(c)
#
# d=re.search("^Rose.*3$",str)
# if d:
#     print("found")
# else:
#     print("not found")
#
#
# d=re.search("^Rose.*4$",str)
# if d:
#     print("found")
# else:
#     print("not found")

#split()
# e=re.split(" ",str) #splits when whitespace encountered
# print(e)
#
# f=re.split("a",str)
# print(f)
#
# g=re.split(" ",str,2) #only does it 2 times then rest is set together
# print(g)


#fullmatch()
# str1="python is a language "
# h=re.fullmatch("python is a language ",str1)
# print(h)

#sub- it replaces one or many matches witha string
# i=re.sub(" ","* ",str1)
# print(i)
#
# j=re.sub(" ","* ",str1,2)
# print(j)


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


# Define a function for
# for validating an Email
def check(email):
    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")


# Driver Code
if __name__ == '__main__':

    email = "ankitrai326@gmail.com"
    check(email)

    email = "my.ownsite@our-earth.org"
    check(email)

    email = "ankitrai326.com"
    check(email)

