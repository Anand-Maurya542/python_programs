cust_list=dict()
n=int(input("enter total number number of customers"))
i=1
while i<=n:
       a=input("enter customer name")
       b=input("enter phone number")
       cust_list[b]=a
       i=i+1
name1=input("enter number::")
del cust_list [name1]
l=cust_list.keys()
print("customer list")
print("name","\t\t\t","phone number")
for i in l:
       print(i,"\t\t\t",cust_list[i])
