# PYTHON FUNCTION TO IMPLEMENT QUEUE DATA
#  STRUCTURE


#Adding elements to queue at the rear end
def insert(data):
   queue.append(data) 


#Removing the front element from the queue
def delete():
   if len(queue)>0:
      return queue.pop(0)
   return "Queue Empty!"


#To display the elements of the queue
def display():
   print("Elements on queue are:");
   for i in range(0,len(queue)):
      print(queue[i])


# function calling
queue=[] 
insert(5)
insert(6)
insert(9)
insert(5)
insert(3)
display()
print("Popped Element is: "+str(delete()))
display()





 
