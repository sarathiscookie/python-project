# Python: dict              - JSON: Object
# Python: tuples, list      - JSON: array
# Python: str               - JSON: string
# Python: int, long, float  - JSON: number
# Python: True              - JSON: true
# Python: False             - JSON: false
# Python: None              - JSON: null

# JSON strings must be written in double quotes.
# dump: method can be used for writing to JSON file.
# load: takes a file object and returns the json object.
# dumps: Convert python object into their respective json string.
# loads: Convert json object into their respective python object.
# Serialization is the process of encoding the from naive data type to JSON format.
# Deserialization is the process of decoding the data that is in JSON format into native data type.

import json

dictionary = {"name": "Peter", "last_name": "Smith", "age": 34, "address": {"city": "Kochi", "state": "Kerala", "country": "India"}, "companies": ["Wipro", "Infosys", "Google", "Amazon"]}

json_string = '{"name": "Peter", "last_name": "Smith", "age": 34, "address": {"city": "Kochi", "state": "Kerala", "country": "India"}, "companies": ["Wipro", "Infosys", "Google", "Amazon"]}'

# Dictionary convert into object.
print("*** Dictionary convert into object ***")
print(dictionary) #{'name': 'Peter', 'last_name': 'Smith', 'age': 34, 'address': {'city': 'Kochi', 'state': 'Kerala', 'country': 'India'}, 'companies': ['Wipro', 'Infosys', 'Google', 'Amazon']}
dictionary_convert_object = json.dumps(dictionary)
print(dictionary_convert_object) #{"name": "Peter", "last_name": "Smith", "age": 34, "address": {"city": "Kochi", "state": "Kerala", "country": "India"}, "companies": ["Wipro", "Infosys", "Google", "Amazon"]}

# List conversion to Array.
print("*** List conversion to Array. ***")
lists = ['Google', 'Amazon', 'Facebook'];
print(lists) #['Google', 'Amazon', 'Facebook']
list_convert_array = json.dumps(lists)
print(list_convert_array) #["Google", "Amazon", "Facebook"]

# tuple conversion to Array.
print("*** Tuple conversion to Array. ***")
tuples = ('one', 'two', 'three')
print(tuples) #('one', 'two', 'three')
tuples_convert_array = json.dumps(tuples)
print(tuples_convert_array) #["one", "two", "three"]

# string conversion to String.
print("*** string conversion to String. ***")
strings = "Hello"
print(strings) #Hello
strings_convert_string = json.dumps(strings)
print(strings_convert_string) #"Hello"

# int conversion to Number.
print("*** int conversion to Number ***")
integer = 5
print(integer) #5
integer_convert_number = json.dumps(integer)
print(integer_convert_number) #5

# float conversion to Number.
print("*** float conversion to Number ***")
float_value = 13.5
print(float_value) #13.5
float_convert_number = json.dumps(float_value)
print(float_convert_number) #13.5

# Boolean conversion to their respective values.
print("*** Boolean conversion to their respective values ***")
print(json.dumps(True)) #true
print(json.dumps(False)) #false

# None value to null.
print("*** None value to null ***") 
print(json.dumps(None)) #null

# Convert json object into their respective python object.
print("*** Convert json object into their respective python object. ***")
person_dict = json.loads(json_string)
print(person_dict) #{'name': 'Peter', 'last_name': 'Smith', 'age': 34, 'address': {'city': 'Kochi', 'state': 'Kerala', 'country': 'India'}, 'companies': ['Wipro', 'Infosys', 'Google', 'Amazon']}
print(person_dict['name']) #Peter

# Convert python object into their respective json object.
print("*** Convert python object into their respective json object. ***")
person_json = json.dumps(person_dict, indent=4)
print(person_json)

"""
Result:
{
    "name": "Peter",
    "last_name": "Smith",
    "age": 34,
    "address": {
        "city": "Kochi",
        "state": "Kerala",
        "country": "India"
    },
    "companies": [
        "Wipro",
        "Infosys",
        "Google",
        "Amazon"
    ]
}
"""

# Serializing JSON data in Python
print("Serializing JSON data in Python.")
with open("dictionaryToJson.json", "w") as dictionaryToJson:
    json.dump(dictionary, dictionaryToJson, indent=4)

# Deserialize JSON to Object in Python.    
print("Deserialize JSON to Object in Python.")
with open("sampleJson.json", "r") as readJsonFile:
    convert_to_python_dictionary = json.load(readJsonFile)
    print(convert_to_python_dictionary['firstName']) #Jane
    print(type(convert_to_python_dictionary)) #<class 'dict'>


