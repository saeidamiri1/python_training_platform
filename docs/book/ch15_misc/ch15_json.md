# Convert a dictionary to a JSON-formatted string:

import json

data = {'first': 1, 'second': 'two', 'third': [3,4,5]}
jj = json.dumps(data)
print(jj)

# Convert JSON string back to a Python dictionary:

d = json.loads(jj)
print(d)


# Save as json 
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

read jason 
with open('data.json', 'rb') as outfile:
    res2 = json.load(outfile)

print(res2) 