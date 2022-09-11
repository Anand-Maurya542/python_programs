num1=0
while num1!=100:
       try:
              num1=eval(input("enter dividend"))
              num2=eval(input("enter divisor"))
              num3=num1//num2
              print("The quotient is=",num3)
       except NameError: print("variable not present")
       except ZeroDivisionError: print("Division by zero not allowed")
       except: print("An error has occured")
       finally: print("Done!!!!")
