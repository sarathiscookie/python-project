from mongo_connect import database

# Collection
collection = database.employees

# Printing the data inserted
cursor = collection.find()
for record in cursor:
    print(record)