n=int(input("enterr any number"))
i=2
f=1
while i<=n-1:
       if n%i==0:
              f=0
              break
       i=i+1
if f==1:
       print(n,"is prime")
else:
       print(n,"is not prime")
