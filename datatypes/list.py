# #mutable, changable, set of elements [], hetrogenoeaus, dupilcates allowed, ordered, indexed
# list1=[1,2,3,"ann"]#a list can have multiple types of data
# # print(list1)
# # print(list1[0])
# #
# # #nested list
# list2 =["ann",[1,2,3]]
# print(list2)
# print(list2[0])
# print(list2[1])
# print(list2[1][1])
# print(list2[-1])#negetive access
#
# #adding and changing element in list
# list2.append('mary')
# print(list2)
#
# list2.remove("mary")
# print(list2)
#
# list2.insert(0,"hello")#(position to insert,"string to insert")
# print(list2)
#
# list3=[1,2,3]
# list4=[5,8,6]
# list3.extend(list4)
# print(list3)
#
#
# list3.pop(2)#if no value is given as parameter then it pops the last value
# print(list3)
#
# list5=list3.copy()
# print(list5)
#
# list4.sort()
# print(list4)
#
# list6=[1,2,3,4,5,2,2,2]
# list6.reverse()
# print(list6)
#
# a=list6.count(2)# counts the occurrence of an element in a list
# print(a)

##########################################################

# listofdict=[{"item":"item1","amt":400},
#             {"item":"item2","amt":600},
#             {"item":"item1","amt":400},
#             {"item":"item2","amt":600}]
# #print(listofdict)
# newdict={}
# list1=[]
# for d in listofdict:
#     p=list(d.values())
#     list1.append(p[0])
#     list1.append(p[1])
#
#
# print(list1)
#
# for i in range(0,len(list1),2):
#     print(i)
#     if list1[i] in newdict:
#         rep=list1[i]
#         index=list1.index(rep)
#         list1[i+1]=list1[i+1]+list1[i+1]
#         newdict[list1[i]]=list1[i+1]
#     else:
#         newdict.setdefault(list1[i],list1[i+1])
# print(newdict)



"""
WAP for python function that takes a list of words and
returns the length of the longest one
"""
list2=["hey","there","im","lauren"]
lenlist=[]
for i in list2:
    leni=len(i)
    lenlist=lenlist.append(leni)
print(lenlist)