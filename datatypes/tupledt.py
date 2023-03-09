# #ordered, unchangable, indexed, allow duplicates, slicable
# tuple1=(1,2,3,4,5,6,"ann",1.3)
# print(tuple1)
#
# #length
# print(len(tuple1))
# list1=[1,2,3,4,5,6,"ann","jose"]
# print(tuple(list1))
# #nested tuple
# nesttuple=(1,2,3,4,5,6,7,8,9,("ann",23))
# print(nesttuple[3])
# print(nesttuple[9][0])
#
# #indexing
# print(nesttuple[3])
# print(nesttuple[-2])
# print("index of ann is ",nesttuple.index(2))
#
# #slicing
# print(nesttuple[1:3])
# print(nesttuple[0:])
# print(nesttuple[::3]) #get every third value
# print(nesttuple[::-3]) #get every third value in reverse order
#
# #updating through mutable data type
# list2=list(tuple1)# first convert to mutable data type
# list2[0]="sam"
# tuple1=tuple(list2)#then covert back to tuple
# print(tuple1)
#
# #append using list
# list2.append("salma")
# tuple1=tuple(list2)
# print(tuple1)
#
# #add a tuple
# tuple2=(10,11)
# tuple1+=tuple2
# print(tuple1)
#
# #remove element through list conversion
# list3=list(tuple1)
# list3.remove("sam")
# tuple1=tuple(list3)
# print(tuple1)
#
# #del---delete tuple
# tuple3=(1,2,3,4,5,6)
# print(tuple3)
# del tuple3
# # print(tuple3)
#
# #unpack tuple
# fruits=("apple","mango","banana","cherry")
# (green,*yellow,red)=fruits
# print(yellow)
#
# #looping in tuple
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)
#
# for i in range(len(thistuple)):
#       print(thistuple[i])
# i=0
# while i < len(thistuple):
#       print(thistuple[i])
#       i = i + 1
#
# #tuple of list
# listtup=(1,2,3,[4,5,6],7)
# print(listtup)
# listtup[3][0]=9 #can change the tuple as we are changing the list part of the tuple
# print(listtup)
#
# #concatenation
# print((1,2,3)+(4,5,6))
#
# #repeat
# print((1,2,3)*3)
#
# #count the occurence
# tuple4=(1,2,3,1,4,6,1,4,2,)
# print("total count of 1 is",tuple4.count(1))
#
# #in
# print(1 in tuple4)
# print(10 in tuple4)
#
# #all
# # returns false if tuple has value-0, or false
# tuple5=(0,1,4,2,3)
# print(all(tuple5))
# print(all(tuple4))
# #min and max
# print(min(tuple5))
# print(max(tuple5))
#
# #enumerate
# name=("ann","sam","dan")
# print(tuple(enumerate(name)))
#
# ages=[23,22,24]
# for i, (name,ages) in enumerate(zip(name,ages)):
#     print(i,name,ages)
#
# #zip
# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")
#
# x = zip(a, b)
# print(tuple(x))
#
# #map
# def myfunc(a, b):
#   return a + b
# d=('orange', 'lemon', 'pineapple')
# c=('apple', 'banana', 'cherry')
# x = map(/yfunc, c, d)
# print(tuple(x))
#
# #others
# print(sorted(tuple5))
# print(sum(tuple5))
#
#
# """
# 1. reverse tuple
# """
# tuple6=(4,2,9,1,0,8)
# print(tuple6[::-1])
#
# """
# 2. tple=(1,2,40,30,20)
#    tple=(1,2,40,[10,20,39],(30,20,10),40)
#
#    to remove elements from this tuple
# to access the value 20 from the tuple
# """
# tuple7=(1,2,40,30,20)
# tuple8=(1,2,40,[10,20,39],(30,20,10),40)
# print(tuple7[4])
# print(tuple8[4][1])
#
# a=[]
# for i in tuple8:
#     if i not in a:
#         a.append(i)
# print(tuple(a))
#
# list1=list(tuple7)
# list1.remove(30)
# print(tuple(list1))

# """
# 3. check if all items in the tuple are the same
# """
# # tuple9=(1,1,1,1)
# tuple9=(1,2,3,4)
# f=1
# for i in tuple9:
#     if tuple9[i] != tuple9[i+1]:
#        f=0
#        break
# if f==1:
#     print("same")
# else:
#     print("not same")
#
#
# #another method
# print(tuple9)
# tuple9=set(tuple9)
# print(tuple9)
# if len(tuple9)==1:
#     print("same")
# else:
#     print("not same")
#
#
#
#
# """
# 4. copy specific elements from one tuple to a new tuple
# """
# tuple10=(3,2,5,1,6,8,2,5,9)
# tuple11=tuple10[2:4]
# print(tuple11)
#
# """
# 5. swap two tuples in python
# """
# # swap tuple9 and tuple7
# tuple9=("a","b","c","d")
# tmp=tuple9
# tuple9=tuple7
# tuple7=tmp
# print(tuple7)
# print(tuple9)
#
#
