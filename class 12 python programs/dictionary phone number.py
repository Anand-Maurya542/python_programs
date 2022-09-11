phone=dict()
i=1
n=int(input("enter number of enteries"))
while i<=n:
       a=input("enter name")
       b=input("enter phone number")
       phone[a]=b
       i=i+1
l=phone.keys()
x=input("enter name to be searched")
for i in l:
       if i==x:
               print(x,": phone number is:",phone[i])
               break
else:
       print(x," does not exist")
