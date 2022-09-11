s=[]
c="y"
while c=="y":
       print("1. Push")
       print("2. Pop")
       print("3. Display")
       choice=int(input("Enter your choice"))
       if choice==1:
              a=input("enter any number:")
              s.append(a)
       elif choice==2:
              if (s==[]):
                     print("Empty stack")
              else:
                     print("Deleted stack is:",s.pop())
       elif choice==3:
              l=len(s)
              for i in range(l-1,-1,-1):
                     print(s[i])
       else:
              print("wrong input")
       c=input("click 'y' for continuing and 'n' for end the program")
