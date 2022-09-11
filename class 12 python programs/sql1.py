import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123" ,database="school")
mycursor=mydb.cursor()
mycursor.execute("Create table shalini(rollno int(3)primary key,name varchar(20),age integer,city char(20))")


