l=eval(input("enter list"))
n=len(l)
print("original list:",l)
for i in range (n):
       for j in range(n-i-1):
              if l[j]>l[j+1]:
                     l[j],l[j+1]=l[j+1],l[j]
print("list after sorting:",l)
