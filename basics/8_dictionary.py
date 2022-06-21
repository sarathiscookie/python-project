# dict(): Key-Value pairs, unordered, mutable, no duplicate key.
# Dictionary: Dictionaries are used to store data values in key:value pairs.
# The popitem() returns and removes an arbitrary element (key, value) pair from the dictionary. Arbitrary elements: An elements not chosen by user.
# pop() return and delete the value of the specified key.

# Creating a blank dictionary
print("*** Creating a blank dictionary ***")
blank_dict = {}
print(blank_dict)

# Creating a dictionary
dictionary = {
  "name": "Peter", 
  "last_name": "Smith", 
  "age": 34, 
  "address": {"city": "Kochi", "state": "Kerala", "country": "India"}, 
  "companies": ["Wipro", "Infosys", "Google", "Amazon"]
}

# Accessing element using get function.
print("*** Accessing a element using get function ***")
print(dictionary.get("companies")) #['Wipro', 'Infosys', 'Google', 'Amazon'] #Type is list

# Accessing element using key
print("*** Accessing a elements using key ***")
print(dictionary["address"]) #{'city': 'Kochi', 'state': 'Kerala', 'country': 'India'}

# Accessing element of a nested dictionary
print("*** Accessing element of a nested dictionary ***")
print(dictionary["address"]["country"]) #India

# Deleting a key from dictionary
print("*** Deleting a key from dictionary ***")
del dictionary["age"]
print(dictionary) #{'name': 'Peter', 'last_name': 'Smith', 'address': {'city': 'Kochi', 'state': 'Kerala', 'country': 'India'}, 'companies': ['Wipro', 'Infosys', 'Google', 'Amazon']}

# Deleting a key from nested dictionary
print("*** Deleting a key from nested dictionary ***")
del dictionary["address"]["state"]
print(dictionary) #{'name': 'Peter', 'last_name': 'Smith', 'address': {'city': 'Kochi', 'country': 'India'}, 'companies': ['Wipro', 'Infosys', 'Google', 'Amazon']}

# Using pop method to return and delete the value of the specified key.
print("*** Using pop method to return and delete the value of the specified key ***")
pop_dict = dictionary.pop("last_name")
print(pop_dict) #Smith
print(dictionary) #{'name': 'Peter', 'address': {'city': 'Kochi', 'country': 'India'}, 'companies': ['Wipro', 'Infosys', 'Google', 'Amazon']}

# Returns and removes an arbitrary element
print("*** Returns and removes an arbitrary element ***")
pop_item_dict = dictionary.popitem()
print(pop_item_dict)
print(dictionary)

# Merge two dictionary
print("*** Merge two dictionary ***")
dict_one = {
  "customer": "Peter",
  "contact": "mobile"
}

dict_two = {
  "profession": "Software Engineer"
}

merge_dict = {**dict_one, **dict_two}
print(merge_dict)

