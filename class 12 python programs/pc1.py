f=0
n=eval(input("enter list"))
x=len(n)
l=int(input("enter number to be searched"))
for i in range(0,x):
       if n[i]==l:
              f=1
              break
if f==1:
       print(l,"number is found at",i+1,"position")
else:
       print(l,"number does not exist")
