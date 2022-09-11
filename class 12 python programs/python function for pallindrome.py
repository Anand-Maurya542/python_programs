def pallindrome(str1):
       length=len(str1)
       i=0
       j=length-1
       f=1
       while i<=j:
              if str1[i]!=str1[j]:
                     f=0
                     break
              i=i+1
              j=j-1
       if f==1:
              print(str1,"is pallindrome")
       else:
              print(str1,"is not pallindrome")
str1=input("Enter string")
pallindrome(str1)
