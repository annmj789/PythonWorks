# f=open("test1","r")
# print(f.read())
# print(f.read(8))
# print(f.readline()) #reads single line
# for i in f:
#     print(i)
# f.close()
# f=open("test1","a")
# f.write("\nhow is your studies going")
# f=open("test1","r")
# print(f.read())
# f=open("test1","w")
# f.write("EVERY THING IS GONE")
# f=open("test1","r")
# print(f.read())

# seek()-sets current file postion it also returns the new position
# f=open("test1","r")
# f.seek(8)
# print(f.read())

#tell()- it returns the current postion of the fille

# f=open("test1","r")
# print(f.tell())
# print(f.readline())
# print(f.tell())

"""
Q. WAP to read a file line by line ans store it into a list
"""
# def fileread(fna):
#     with open(fna) as f:
#         oplist=f.readlines()
#     print(oplist)
# fileread("test1")


#to copy a text to another
# from shutil import copyfile
# copyfile("test1","test2")

# str0="man lan can ran man lan can pan dan"
# list=str0.split(" ")
# d={}
# for i in list:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

f=open("test1","r")
dict={}
for i in f:
    var=i.split(" ")
    for j in var:
        if j not in dict:
            dict[i] = 1
        else:
            dict[i] += 1

print(dict)
