f=0
l=eval(input("enter a list of 10 elements"))
n=int(input("enter number you want to search"))
le=len(l)
for i in range (0,le):
       if n==l[i]:
              f=1
              break
if f==1:
       print(n,"is found at",i+1,"position")
else:
       print(n,"is not found")
