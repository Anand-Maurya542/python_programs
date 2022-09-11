L=[10,"Fun",40,"Few",50,"Full"]
for i in range (len(L)):
       if type(L[i])==int:
              L[i]=L[i]**2
       elif type(L[i])==str:
              L[i]=(L[i]).swapcase()
print(L)
       
