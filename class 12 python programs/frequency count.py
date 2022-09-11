L=eval(input("enter list"))
L1=[]
L2=[]
for  i in L:
       if i not in L2:
              x=L.count(i)
              L1.append(x)
              L2.append(i)
print("elements","\t\t\t","frequency")
for i in range(len(L1)):
       print(L2[i],"\t\t\t",L1[i])
