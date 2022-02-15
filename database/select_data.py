from distutils.sysconfig import customize_compiler
import mysql.connector 

from mysql.connector import errorcode

from mysql_connect import data_base

cursor_object = data_base.cursor()

select_data = "SELECT name, email, city, mobile FROM users"
cursor_object.execute(select_data)

result  = cursor_object.fetchall()

for data in result:
    print(data) 

# disconnection from server
data_base.close()    