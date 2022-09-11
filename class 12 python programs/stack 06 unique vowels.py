vowels=["a","e","i","o","u","A","E","I","O","U"]
word=input("Enter the word to search for vowels:")
stack=[]
for letter in word:
       if letter in vowels:
              if letter not in stack:
                     stack.append(letter)
print(stack)
print("The number of different vowels present in ", word,"is",len(stack))
