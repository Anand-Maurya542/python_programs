# python function to perform PUSH() and POP() operation on stack.
def isEmpty(stk): # checks whether the stack is empty or not
   if stk==[]:
      return True
   else:
      return False
# WRITE PYTHON FUNCTION TO ADD ELEMENTS IN STACK
def Push(stk,item): # Allow additions to the stack
   stk.append(item)
   top=len(stk)-1
# WRITE PYTHON FUNCTION TO REMOVE ELEMENTS IN STACK
def Pop(stk):
   if isEmpty(stk): # verifies whether the stack is empty or not
      print("Underflow")
   else: # Allow deletions from the stack
      item=stk.pop()
      if len(stk)==0:
         top=None
      else:
         top=len(stk)
         print("Popped item is "+str(item))
# FUNCTION TO DISPLAY STACK
def Display(stk):
   if isEmpty(stk):
      print("Stack is empty")
   else:
      top=len(stk)-1
      print("Elements in the stack are: ")
      for i in range(top,-1,-1):
         print (str(stk[i]))

# FUNCTION CALLING
stk=[]
top=None
Push(stk,1)
Push(stk,2)
Push(stk,3)
Push(stk,4)
Display(stk)
Pop(stk)
Display(stk)
