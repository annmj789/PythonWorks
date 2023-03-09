# #print a right triangle pyramid
# row=int(input("Enter the number of rows"))
# for i in range(0,row+1):#row
#     for j in range(i):#coloum
#          print("*",end=" ")
#     print()
#############################################################################################
# #print a number regular triangle pyramid
# row=int(input("Enter the number of rows"))
# for i in range(0,row+1):#row
#     for k in range(row-i):#space
#          print(" ",end="")
#     for j in range(i):#colomn
#          print(i,end=" ")
#     print() # used for newline
# #############################################################################################
# # print reverse
# row=int(input("Enter the number of rows"))
# for i in range(0,row+1):#row
#     for j in range(row-i):#coloum
#          print(i+1,end=" ")
#          i = i + 1
#     print()
############################################################################################
# row=int(input("Enter the number of rows"))
# for i in range(0,row+1):#row
#     for j in range(i):#coloum
#          print(j+1,end=" ")
#          i = i + 1
#     print()

############################################################################################
# #diamond
# row=int(input("Enter the number of rows"))
# for i in range(0,row+1):#row
#     for k in range(row-i):#space
#          print(" ",end="")
#     for j in range(i):#colomn
#          print(i,end=" ")
#     print() # used for newline
# for i in range(1,row+1):#row
#     for k in range(i):#space
#          print(" ",end="")
#     for j in range(row-i):#colomn
#          print(row-i,end=" ")
#     print() # used for newline

############################################################################################
# #alphabet right triangle
# k=0
# row=int(input("Enter the number of rows"))
# ch=chr(65)
# for i in range(0,row+1):#row
#      for j in range(i):#coloum
#          print(ch,end=" ")
#          k=k+1
#          ch = chr(65+k)
#      print()
############################################################################################
# #alphabet regular triangle
# l=0
# ch=chr(65)
# row=int(input("Enter the number of rows"))
# for i in range(0,row+1):#row
#     for k in range(row-i):#space
#          print(" ",end="")
#     for j in range(i):#colomn
#         print(ch, end=" ")
#         l=l+1
#         ch = chr(65+l)
#     print()
############################################################################################
# #reverse diamond
# row=int(input("Enter the number of rows"))
# for i in range(0,row):#row
#     for k in range(i):#space
#          print(" ",end="")
#     for j in range(row-i):#colomn
#          print("*",end=" ")
#     print() # used for newline
# for i in range(2,row+1):#row
#     for k in range(row-i):#space
#          print(" ",end="")
#     for j in range(i):#colomn
#          print("*",end=" ")
#     print() # used for newline
############################################################################################
# #hollow diamond
# row=int(input("Enter the number of rows"))
# for i in range(0,row):#row
#     print("   " * (row - i) + "*", end=" ")
#     if i != 0:
#         print("   " * (2 * i) + "*", end=" ")
#     print()
# for i in range(row, -1,-1):  # row
#     print("   " * (row - i) + "*", end=" ")
#     if i != 0:
#         print("   " * (2 * i) + "*", end=" ")
#      print()
# 333#######################################################################
# #print a odd number regular triangle pyramid
# row=int(input("Enter the number of rows"))
# row=row+2
# for i in range(1,row+1):#row  1 2 3 4 5
#   if i%2!=0:
#       for k in range(row-i):#space
#          print(" ",end="")
#       for j in range(i):#colomn
#          print("@",end=" ")
#       print() # used for newline

############################################################################
# hallow square
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        ch=chr(64+i)
        if(i==1 or i==n or j==1 or j==n):
            print(ch, end=" ")
        else:
           print(" ",end=" ")
    print("")
