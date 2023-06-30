import pymysql
conn=pymysql.connect(host='localhost',user="root",db="hotel")
print("Connection Established")
mycursor=conn.cursor()
#query="create table customer_detail (id int primary key,name varchar(25))"
#ins="insert into customer_detail (name) values('Ram')"
#upd="update customer_detail set name='Shyam' where id=1"
cuname="Rohan"

query = "insert into customer_detail (name) values(%s);"
val = (cuname)
mycursor.execute(query,val)
#mycursor.execute(upd)
conn.commit()
print("data inserted successfully")
conn.close()