v=['a','e','i','o','u']
word=input("enter word")
s=[]
for letter in word:
       if letter in v:
                     s.append(letter)
print(s)
print(len(s))
                     
