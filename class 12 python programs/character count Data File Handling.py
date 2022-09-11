def func(l):
       c=0
       for line in l:
              if line[0]=="A" or "a":
                     c+=1
       return c
f=open("Lines.txt","r")
l=f.readlines()
print(func(l))
