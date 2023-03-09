a=int(input("enter the number"))
b=int(input("enter the number"))
c = int(input("enter the number"))#input()- input function in python

if a>b and a>c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
elif c>a and c>b:
    print("c is greatest")
else:
    print("equal")

#nested if
a=5
if a>1:
    print("a is larger than 1")
    if a>2:
        print("a is larger than 2")
    else:
        print("a is not larger than 2")
else:
    print("a is not larger than 1")
