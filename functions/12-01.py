"""
1. Create function to create List
2. Search en item in a List
3. Remove an element from a list
4. To replace an element with new element
"""

#1
list1=[]
def createL(size):
    for i in range(size):
     ele = input("Enter the element: ")
     list1.append(ele)
    print(list1)

size=int(input("Enter size: "))
createL(size)

#2

list2=[2,2,3,4,5,6]
def searchL(search):

        if search in list2:
            print("found")
        else:
            print("Not found")

search=int(input("Enter the element to be searched: "))
searchL(search)


#3

rmele=int(input("Enter the element to be removed"))
if rmele in list2:
    list2.remove(rmele)
    print("Removed")
else:
    print("Not found")
print(list2)

#4

def replaceL(old,new):
    for i in range(len(list2)):
        if list2[i]==old:
            list2[i]=new

    print(list2)

old = int(input("Enter the element to be replaced: "))
new = int(input("Enter the new element: "))
replaceL(old,new)