def fibo():
       num=int(input("Enter the limit"))
       x=0
       y=1
       z=0
       while z<=num:
              print(z,end=" ")
              x=y
              y=z
              z=x+y
              print("\n")
fibo()
