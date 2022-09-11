def read_bin():
       import pickle
       f=open("aman.dat","rb")
       l1=pickle.load(f)
       print(l1)
       f.close()
read_bin()
