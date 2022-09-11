a=int(input("enter first number"))
b=int(input("enter second number"))
op=input("enter any operator:+,-,*,/,//,%")
if op=="+":
       print("sum=",a+b)
elif op=="-":
       print("difference=",a-b)
elif op=="*":
       print("product=",a*b)
elif op=="/":
       print("division=",a/b)
elif op=="//":
       print("quotient=",a//b)
elif op=="%":
       print("mod=",a%b)
else:
       print("invalid input")
