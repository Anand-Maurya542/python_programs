def push(l,item):
       l.append(item)
       return l
def pop(l):
       if l==[]:
              print("Empty stack")
       else:
              x=l.pop()
       return x
def display(l):
       x=len(l)
       print("element are:")
       for i in range(x-1,-1,-1):
              print(l[i])

l=[]
print(push(l,45))
print(push(l,54))
print(push(l,87))
print("Deleted element is: ",pop(l))
display(l)
