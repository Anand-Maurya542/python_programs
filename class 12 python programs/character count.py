word=input("enter any sentence")
c=0
for letter in word:
       if letter in ('i','a','e','o','u'):
              c=c+1
print("number of vowels=",c)
x=word.split()
cnt=0
for i in x:
       cnt=cnt+1
print("number of words=",cnt,x)
l=len(word)
print("number of character (including spaces)=",l)
