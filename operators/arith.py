#arith
a=5
b=9
print(a+b)
print(a-b)
print(a*b)

#logical
print(a>b)
print(not(a>b))

#identity
#is
#is not
a=["apple","banana"]
b=["apple","orange"]
c=a
print(a is b)#false because objects are different
print(a is c)#true

#membership
print("apple" in a) #true
print("mango" in a) #false