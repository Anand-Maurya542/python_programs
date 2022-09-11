#to count words 'to' and 'the ' present in the file
f=open("poem.txt","r")
c_to=0
c_the=0
for line in f:
       c_to+=line.count("to")
       c_the+=line.count("the")
print(c_to)
print(c_the)
