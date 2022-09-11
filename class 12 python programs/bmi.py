h=float(input("enter height in metre"))
w=float(input("enter weight in kg"))
b=0
b=w//(h**2)
print("your BMI is ",b)
if 16<=b<=20:
       print("you are underweight")
if 20<b<=25:
       print("normal")
if 25<b<=30:
       print("you are overweight")
if b>30:
       print("obese")
