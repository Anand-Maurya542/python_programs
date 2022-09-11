t1=tuple()
n=int(input("enter total number of elements"))
for i in range(n):
        a=int(input("enter total values"))
        t1=t1+(a, )
sd=ld=t1[0]
for i in range(n):
       if t1[i]>ld:
              ld=t1[i]
       if t1[i]<sd:
              sd=t1[i]
print("smallest digit=",sd)
print("largest digit =",ld)
