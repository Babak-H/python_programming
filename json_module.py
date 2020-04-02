# JSON
# JavaScript Object Notation

import json

people_string = '''
{
    "people": [
        {
            "name" : "john smith",
            "phone" : "123-456-7890",
            "email" : ["john@gmail.com", "smith@yahoo.com"],
            "has_licence" : false
        },
        {
            "name" : "Jane Doe",
            "phone" : "560-555-5153",
            "email" : null,
            "has_licence" : true
        }
    ]
}
'''

# a json object will be converted to python dictionary
data = json.loads(people_string)

print(type(data))
print(type(data['people']))

for person in data['people']:
    print(person['name'])

# here we delete phone number from data and then turn it back into a json object
for person in data['people']:
    del person['phone']

# indent will make the json file more readable
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

# ============================
# load json from a file, edit it, then save it in another file

with open("./Files/states.json") as f:
    data = json.load(f)

for state in data['states']:
    #print(state['name'], state['abbreviation'])
    del state['abbreviation']

with open("./Files/new_states.json", "w") as f:
    json.dump(data, f, indent=2)

# =============================
# download json from a web api
from urllib.request import urlopen

with urlopen("https://jsonplaceholder.typicode.com/todos") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=2))
# print(len(data))
# print(data[0])

completed_dict = {}
for dat in data:
    id = dat['id']
    if dat['completed'] == True:
        completed_dict[id] = dat['title']

# to save as json file it would be better to save as list, then each row would be its 
# own dict
with open("./Files/to_do.json", "w") as f:
    json.dump(completed_dict, f, indent=2)








