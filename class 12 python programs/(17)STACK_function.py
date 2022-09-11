# PYTHON FUNCTION TO IMPLEMENT STACK DATA STRUCTURE

def  isEmpty(stk): # checks whether the stack is empty or not
      if  stk  == []:
            return True
      else:
            return False

#  python function to add elements in stack
def   Push(stk, item): 
      stk.append(item)
      top  =  len(stk)  -  1


# python function to remove elements from stack
def  Pop(stk):
      if  isEmpty(stk):
               print("Underflow")
      else: 
               item=stk.pop()
               if len(stk)==0:
                     top=None
               else:
                     top=len(stk)
                     print("Popped item is "+str(item))


# function to display stack
def Display(stk):
   if isEmpty(stk):
      print("Stack is empty")
   else:
      top=len(stk)-1
      print("Elements in the stack are: ")
      for i in range(top,-1,-1):
         print (str(stk[i]))

# function calling
stk=[]
top=None
Push(stk,1)
Push(stk,2)
Push(stk,3)
Push(stk,4)
Display(stk)
Pop(stk)
Display(stk)
