n=int(input("enter a number"))
rev=0
x=n
while n>0:
       a=n%10
       rev=(rev*10)+a
       n=n//10
if x==rev:
       print("pallindrome")
else:
       print("not pallindrome")
