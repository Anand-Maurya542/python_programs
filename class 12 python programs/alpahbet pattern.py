ch=65
r=int(input("enter total rows"))
for i in range(1,r+1):
       ch=65
       for j in range(0,i):
              print(chr(ch),end="")
              ch=ch+1
       print( )
