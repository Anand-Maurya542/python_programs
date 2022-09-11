print("1. change temperature from celsius to fahrenheit")
print("2. change temperature from fahrenheit to celsius")
print("3. exit")
ch=int(input("enter your choice"))
if ch==1:
       c=float(input("enter temperature in celsius"))
       f=0
       f=(9/5*c)+32
       print("temperature in fahrenheit is",f)
elif ch==2:
       f=float(input("enter temperature in fahrenheit"))
       c=0
       c=(f-32)*5/9
       print("temperature in celsius is",c)
else:
       print("exit")
