import csv
fields=["Name","Class","Year","Percentage"]
rows=[["Rohit","12th","2003","92"],
             ["Shanupriya","11th","2004","82"],
             ["Deep","12th","2002","80"],
             ["Prerna","11th","2006","85"],
             ["Lakshya","12th","2005","72"]]
filename="marks.csv"
with open(filename,"w",newline='') as f:
       csv_w=csv.writer(f, delimiter=",")
       csv_w.writerow(fields)
       for i in rows:
              csv_w.writerow(i)
       print("File created")
