from pymongo import MongoClient

try:
    client = MongoClient("localhost", 27017, username="root", password="secret")
    print("Connected Successfully!")
except:
    print("Could not connect to MongoDB")

# Database
database = client.company
