l=eval(input("enter number of elements"))
sum=0
mean=0
length=len(l)
for i in range(length):
       sum=sum+l[i]
       i=i+1
       mean=sum/length
print("mean=",mean)
