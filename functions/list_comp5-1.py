
"""
provides an easy way to operate on list. it creates a new list in which each element is the result of applying a given operation on a list
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

hletters=[y for y in "human"]
print(hletters)


"""seperate range of 100 numbers to even and odd list"""


# even=[e for e in range(101) if e%2==0]
# odd=[e for e in range(101) if e%2!=0]
# print(even)
# print(odd)

""""Sum of n natural numbers"""
# n=input("Enter any number")
# totsum=0
# sum=((n*(n+1)/2) for s in range(n))
#
# print(sum)

n="Ann Mary Jose"
f=n.split(  )
print(f)

colors=['red','white', 'indigo','pink',"blue"]
listE=list([i for i in colors if "e" in i])
print(listE)