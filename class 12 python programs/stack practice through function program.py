s=[]
top= None
def isEmpty(stk):
       if (stk==[]):
              return True
       else:
              return False
def push(stk,item):
       stk.append(item)
       top=len(stk)-1
def s_pop(stk):
       if (isEmpty(stk)):
              return ("Underflow")
       else:
              i=stk.pop()
              if (len(stk)==0):
                     top= None
              else:
                     top=len(stk)
                     print("Popped item is "+str(item))


def peek(stk):
       if (isEmpty(stk)):
              return ("Underflow")
       else:
              top=len(stk)-1
              return stk[top]
def display(stk):
       if (isEmpty(stk)):
              print("Stack is empty")
       else:
              top=len(stk)-1
              print(stk[top],"<......top")
              for  i in range (top-1,-1,-1):
                     print(stk[i])
while True:
       print("stack Implementation")
       print("1. Push")
       print("2. Pop")
       print("3. Peek")
       print("4. Display")
       print("5. Exit")
       ch=int(input("Enter the choice (1-5)"))
       if ch==1:
              item=int(input("Enter the item you want to push:"))
              push(s,item)
              print("%d added successfully"%item)
              input("press any key to continue")
       elif ch==2:
              item=s_pop(s)
              if item== 'Underflow':
                     print("Stack is Empty")
              else:
                     print("%d is popped"%item)
              input("press any key continue")
              
       elif ch==3:
              item=peek(s)
              if item== 'Underflow':
                     print("Stack is Empty")
              else:
                     print("%d is at the top"%item)
              input("press any key continue")
              
              
       elif ch==4:
              display(s)
              input("press any key to continue")

       elif ch==5:
              break
       else:
              print("Andhe 1-5 tak daalna tha ")



              
