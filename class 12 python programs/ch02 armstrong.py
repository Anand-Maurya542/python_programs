def arms(n):
       s=0
       x=n
       while n>0:
              r=n%10
              s=s+r**3
              n=n//10
       if x==s:
              print("Number is armstrong")
       else:
              print("number is not armstrong")
n=int(input("enter number"))
arms(n)

              
