import mysql.connector as sqltor1
conn=sqltor1.connect(
    host ="localhost",
    user="root",
    password="12345"
    )
if conn.is_connected ():
    print("Sucessfully connected")

conn.cursor().execute("CREATE DATABASE showroom")
print("Dtabase Successfully Created")
conn.cursor().execute("USE showroom")
conn.cursor().execute('create table log_in(cust_name  varchar(65),account_no  int, password int)')
print("Log_in table created")
conn.cursor().execute('create table customer_table(f_name varchar(65),cloth_code bigint,price int,size varchar(10),phone_no bigint )')
print("customer_table created")
conn.commit()
print("DONE")
