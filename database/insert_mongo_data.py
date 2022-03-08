from mongo_connect import database

# Collection
collection = database.employees

emp_det_1 = {
    "name": "Smith",
    "eid": 1005,
    "branch":"chennai"
}

emp_det_2 = {
    "name": "Doe",
    "eid": 1006,
    "branch":"kerala"
}

# Insert Data
collection.insert_one(emp_det_1)
collection.insert_one(emp_det_2)

print(f"Data inserted with record ids {emp_det_1}, {emp_det_2}")

