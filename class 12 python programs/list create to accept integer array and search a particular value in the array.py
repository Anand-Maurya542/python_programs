L=[10,20,3,100,65,87,2]
N=int(input("enter the number to be searched:"))
for i in range (len(L)):
       if type(L[i])==int and L[i]==N:
              print("exists at position:",i+1)
              break
else:
       print("does not exist")
