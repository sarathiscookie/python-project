from mysql_connect import data_base

# Preparing a cursor object. 
cursor_object = data_base.cursor()

store_user = "INSERT INTO users (name, email, city, mobile) VALUES (%s, %s, %s, %s)"
user_value = ("Peter", "peter@gmail.com", "Europe", "23423423423")

cursor_object.execute(store_user, user_value)
data_base.commit()
    
# disconnection from server
data_base.close()
    