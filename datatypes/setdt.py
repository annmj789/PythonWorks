"""
1. immutable
2. Unordered
3. Unindexed
4. Duplicates not allowed

set item are unchangable, but you can remove iterms and items
"""
# set1={1,2,3,4}
# print(set1)
# set2=set({1,2,3,(4,5,6),[7,8,9]})
# # print(set2)
# print(set2)

"""
1. Add a list of elements of a set
2. get only unique items from two sets
3. check if two sets have any elements in common. if yes, display the common elements
4. remove items from set1 that re not common to both set1 and set2
"""
#1. Add a list of elements of a set
setA={1,2,3,4}
sample=[5,6,7,8]

setA.update(sample)
print("1",setA)

#2. get only unique items from two sets
set2={1,2,2,4,4,5}
set3={3,2,5,6,7,7,1}

print("2",set2.union(set3))

#3. check if two sets have any elements in common. if yes, display the common elements
set5=set3.intersection(set2)
if set3.isdisjoint(set2):
    print("no common elements")
else:
    print("3",set5)

#4. remove items from set1 that are not common to both set1 and set2
set6={1,2,4,5}
set7={3,2,5,6,7,1}
print("4",set6.difference_update(set7))
print("4",set2.intersection(set3))