import pymysql

# connection establish
conn=pymysql.connect(host="localhost",user="root",db="dream")
mycursor=conn.cursor()
print("connection established")
query="create table dream (Name varchar(20),age varchar(3))"
'''a="insert into dream (Name,age) values('Brijesh','17')"
mycursor.execute(a)'''
b="update dream set age='16' where name='Brijesh'"
#mycursor.execute(ins)
conn.commit() # to save the changes into database
print("table data updated successfully")

