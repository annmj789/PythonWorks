try:
    n1=int(input("Enter first number: "))
    n2=int(input("Enter second number: "))
    n3=n1/n2
    print("Answer: ",n3)
except ZeroDivisionError as er:
    print(er)
except ValueError as vr:
    print(vr)