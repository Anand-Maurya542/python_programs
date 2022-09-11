import csv
f=open("student.csv","r")
r=csv.reader(f)
rec=[]
for x in r:
       rec.append(x)
print(len(rec)-1)
f.close()
