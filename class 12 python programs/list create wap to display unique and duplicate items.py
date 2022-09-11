L1=[2,7,1,4,9,5,1,4,3]
L2=[]
L3=[]
for i in L1:
       if i not in L2:
              L2.append(i)
       else:
              L3.append(i)
print(L2)
print(L3)
