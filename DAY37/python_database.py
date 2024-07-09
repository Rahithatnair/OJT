
#python database handling
import sqlite3
conn = sqlite3.connect('articllle.db')
c=conn.cursor()
conn.close

import sqlite3
conn = sqlite3.connect('articllle.db')
c=conn.cursor()
c.execute("create table example(Software VARCHAR, Version Real,Price Real )")

c.execute("Insert into example Values('Python',3.4,'100')")
c.execute("Insert into example Values('Adobe',10.2,'1000')")
c.execute("Insert into example Values('Office',16,'1000')")

sql = "select * from example"
for row in c.execute(sql):
    print("Software: "+row[0])
    print("Version: "+str(row[1]))
    print("Price: "+str(row[2]))
    
def dynamic_data():
    soft = input("Write Software Name : ")
    version = input("Write Versio : ")
    Price= input("Write Price")    
    c.execute("insert into example(Software,Version,Price) values(?,?,?)" ,(soft,version,Price))
    conn.commit()
dynamic_data()

sql="update example set Version = 3.5 where Software = 'Python'"
c.execute(sql)
sql = "select * from example"
for row in c.execute(sql):
    print(row)


sql="delete from example where Software= 'Python'"
c.execute(sql)
sql = "select * from example"
for row in c.execute(sql):
    print(row)