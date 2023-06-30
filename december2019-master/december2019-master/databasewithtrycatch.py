import pymysql
conn=None
try:
    conn = pymysql.connect(host="localhost", user="root", db="hotel")
    mycursor = conn.cursor()
    sql_select_Query = "select * from customer_detail"

    mycursor.execute(sql_select_Query)
    records = mycursor.fetchall()
    print(records)
    print("Total number of rows in customer_detail is - ", mycursor.rowcount)
    print("Printing each row's column values i.e.  customer_detail record")
    for row in records:
        print("id = ", row[0] )
        print("name = ", row[1],"\n")

    mycursor.close()

except ValueError as e:
    print("Error while connecting to MySQL", e)
finally:
   conn.close()
   print("MySQL connection is closed")