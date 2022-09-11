n=int(input("enter any number"))
rev=0
x=n
while n>0:
       r=n%10
       rev=(rev*10)+r
       n=n//10
print("reverse digit=",rev)
if x==rev:
       print("no. is pallindrome:")
else:
       print("no. is not pallindrome")
