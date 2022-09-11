r=int(input("enter total rows"))
for i in range(r,0,-1):
       for j in range (0,r-i):
              print(" ",end=" ")
       for j in range(0,i):
              print("*",end=" ")
       for j in range(0,i-1):
              print("*",end=" ")
       print()
