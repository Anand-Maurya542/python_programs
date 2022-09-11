i=1
s=0
num=int(input("enter a number"))
while i<num:
       if num%i==0:
              s+=i
       i=i+1
if s==num:
       print("it is a perfect number")
else:
       print("it is not a perfect number")
