t1=tuple()
n=int(input("enter total elements"))
for i in range (n):
       a=int(input("enter values"))
       t1=t1+(a, )
print(t1)
f=0
num=int(input("enter number you want to search"))
for i in range (n):
       if num==t1[i]:
              f=1
              break
if f==1:
       print(num,"is found at",i+1,"position")
else:
       print(num,"not found")
