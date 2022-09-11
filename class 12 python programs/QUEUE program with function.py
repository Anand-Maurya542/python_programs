# Python user defined functions to implement queue
# using list
#Adding elements to queue at the rear end

def insert(data): # function with parameter
   queue.append(data) # append=add at the end

#Removing the front element from the queue
def delete():
   if len(queue)>0:
      return queue.pop(0) # pop(0) =remove element from 0 index
   return ("Queue Empty!")

#To display the elements of the queue
def display():
   print("Elements on queue are:");
   for i in range(0,len(queue)):
      print(queue[i])

# function calling
queue=[]  # empty list
insert(5)
insert(6)
insert(9)
insert(5)
insert(3)
print("Elements of queue are ")
display()
print("Popped Element is: "+str(delete()))
display()





 
