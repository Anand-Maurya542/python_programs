def binary_file_reading():
       f=open("bfile.dat","rb")
       num=list(f.read())
       print(num)
       f.close()
binary_file_reading()
