"""
lambda funtion
anonymous function. It can take any number of argument but can only have one expression.
difference bw regular and lamda fn

"""

# regular fn
def sum(a,b):
    return a+b

print(sum(3,2))

#corressponding lambda fn
#syntax: lambda arguments:expresion
add=lambda a,b:a+b
print(add(2,3))

largest=lambda a,b:a if(a>b) else b
print(largest(2,4))


#filter- removes elements that does not satisfies the condition
list1=[1,2,3,4,5,6]
listF=list(filter(lambda x:x%2==0,list1))
print(listF)

#map - applies expression on all elements and returns it
listm=list(map(lambda x:x%2==0,list1))
print(listF)
listM=list(map(lambda x:x*2,list1))
print(listF)

#reduce

from functools import reduce
listR=reduce(lambda x,y:y+x,list1)
print(listR)