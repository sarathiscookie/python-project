import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

for user in response.json():
    print(f"Name: {user['name']}, Email: {user['email']}, Website: {user['website']}, Phone: {user['phone']}, Address: {user['address']['street']}")

