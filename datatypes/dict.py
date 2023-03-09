#mapping dta type- key value pairs in  {}, duplicated not allowed for keys, indexed, ordered, mutable- changable

dict={"name":"ann",
      "age":23,
      "address":"TCR",
      "DOB":"7-8-99"}
# print(dict)


##to get value
#
# es of particular keys
# x=dict["name"]
# m=dict.get("name")
# print(m)
# print(x)

# #to print all keys
# x=dict.keys()
# print(x)

# #to print all values
# x=dict.values()
# print(x)

# #to print key and values together as items
# x=dict.items()
# # print(x)
#
# # to change the value of a key
# dict["name"]="helen"
#
# x=dict.items()
# print(x)

# #update
# dict.update({"age":24})
# print(dict.items())
# dict.update({"age":25}{"name":"riley"})
# print(dict.items())

# #add new items
# dict["course"]="CS"
# print(dict.items())
# dict.update({"color":"red"})
# print(dict.items())

# #to remove
# dict.popitem()
# print(dict.items())
# dict.pop("name")
# print(dict.items())

# #to delete complete dictionary
# del dict
# print(dict)

# #to clear, here the data will be deleted no the dictionary
# dict.clear()
# print(dict)
##############################################################################
# #to access dictionary using loop
# for i in dict():
#       print(i)
#
# for i in dict.values():
#       print(i)
#
# for i in dict.items():
#       print(i)

#############################################################################
# #nested dictionary
# dict1={
#       "personal":{
#             "name":"ann",
#             "age":23,
#             "DOB":"7-8-99"
#              },
#       "address":{
#             "dstrict":"TCR",
#             "pin":680683
#              },
#       }
# print(dict1["personal"])
# print(dict1["address"]["pin"])
# print(dict1.values())
# print(dict1["personal"].values())
# dict1.update({"academics":{"rank":4}})
# print(dict1)
# dict1["personal"]["name"]="sam"
# # print(dict1)
# print(dict1.get("address"))
# print(dict1["address"].get("dstrict"))
# print(dict1)

# dict2={"Name":"Ann",
#        "Age":23,
#        "Name":"Sandra"
#        }
# for i in dict2.values():
#       print(i)
#############################################################

# dict1={1:["Ann","DS"],
#        2:["Sam","java"]}
# print(dict1.values())
# print("NAME \t  SUBJECT")
# for i in dict1.values():
#       print("{:<10} {:<10}".format(i[0],i[1]))
#       # print(f'{name} is {age} years old')

# dict2={"name":"ann","age":23}
# print(dict2.items())
# for i in dict2.items():
#     print (i[0],":",i[1])
# ###############################################################################
# dic = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# uni = set() #set doesnt allow duplicate value
#
# for i in dic:
#     for value in i.values():
#         uni.add(value)
# print(uni)
# ############################    OR    ###############################################
# list1=[]
# for i in dic:
#     list1.extend(list(i.values()))
# list1=set(list1)
# print(list1)
#
#
###################################################################################
# #question: convert each letter in string as values in a dictionary
# str="luminar python"
# dict2={}
# for i in range(1,len(str)+1):
#     dict2.setdefault(i,str[i-1])
# print(dict2.items())

###################################################################################
# # sort distionary based on its values
# dict0={1:2,3:4,4:3,2:1,0:0}
# desc={}
# aesc={}
# val=[]
# val1=[]
# key=[]
# val=list(dict0.values())
# key=list(dict0.keys())
# val.sort()
# for i in val:
#       index=list(dict0.values()).index(i)
#       aesc[key[index]]=i
# val.sort(reverse=True)
# for i in val:
#       index = list(dict0.values()).index(i)
#       desc[key[index]] = i
# print("Aescendinf order",aesc.items(),"Descending order",desc.items())
#
dict0={1:2,3:4,4:3,2:1,0:0}
