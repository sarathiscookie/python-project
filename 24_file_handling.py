import json

f = open("sampleJson.json", "r")

data = json.load(f)

for children in data['children']:
    print(children['firstName'])

f.close()