library=[]
c="y"
while (c=="y"):
       print("1. Insert")
       print("2. Delete")
       print("3. Display")
       choice=int(input("Enter your choice:"))
       if choice==1:
              bid=input("enter book id")
              bname=input("enter book name")
              lib=(bid,bname)
              library.append(lib)
       elif choice==2:
              if library==[]:
                     print("Queue empty")
              else:
                     print("Deleted element is:",library.pop(0))
       elif choice==3:
              l=len(library)
              for i in range(0,l):
                     print(library[i])
       else:
              print("Wrong output")
       c=input("Do you want to continue or not")
