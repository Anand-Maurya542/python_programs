l=eval(input("enter a list"))
f=0
ln=len(l)
n=int(input("enter number to searched"))
for i in range (0,ln):
       if l[i]==n:
              f=1
              break
if f==1:
       print(n,"is found at",i+1,"position")
else:
       print(n,"is not found")
