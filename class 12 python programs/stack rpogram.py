def push(stack,x):
       stack.append(x)
def pop(stack):
       if len(stack)<=0:
              print("Stack is empty")
       else:
              stack.pop()
def display(stack):
       if len(stack)<=0:
              print("Nothing to display ,stack is empty")
       else:
              for i in range(len(stack)-1,-1,-1):
                     print(stack[i])
x=[]
choice=0
while choice!=4:
       print("stack menu")
       print("press 1 for insert")
       print("press 2 for pop")
       print("press 3 for display")
       print("press 4 for exit")
       choice= int(input("enter your choice"))
       if choice==1:
              value=int(input("enter 'value"))
              push(x,value)
       if choice==2:
              pop(x)
       if choice==3:
              display(x)
       if choice==4:
              print("you selected to close this program")
              
