print("1. to calculate the area of circle")
print("2. to calculate the area of rectangle")
print("3. to calculate the circumference of circle")
print("4. to calculate the area of square")
print("5. exit")
ch=int(input("enter your choice"))
if ch==1:
       r=float(input("enter radius of circle"))
       a=0
       a=3.14*r*r
       print("area of circle is ",a)
elif ch==2:
       l=float(input("enter length of rectangle"))
       b=float(input("enter breadth of rectangle"))
       a=0
       a=l*b
       print("area of rectangle is ",a)
elif ch==3:
       r=float(input("enter radius of circle"))
       c=0
       c=2*3.14*r
       print("circumference of circle is ",c)
elif ch==4:
       a=float(input("enter side length of square"))
       ar=0
       ar=a*a
       print("area of square is ",ar)
elif ch==5:
       print("Invalid input")
       print("exit")
