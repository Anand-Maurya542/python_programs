str=input("enter the string")
l=len(str)
p=l-1
index=0
while (index<p):
       if (str[index]==str[p]):
              index=index+1
              p=p-1
       else:
              print("string is not pallindrome")
              break
else:
       print("string is a pallindrome ")
