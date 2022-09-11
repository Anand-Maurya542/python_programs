def file_copy():
       f1=open("fact.py","r")
       f2=open("Anand.py","w")
       str1=f1.read()
       f2.write(str1)
       f1.close()
       f2.close()
       print("copying done")
file_copy()
