
# JSON has no end tag, no start tag, and no attributes
import json
data = '''
[
 {"id" : "001",
  "x" : "2",
  "name" : "Ken"
 },
 {"id" : "002",
  "x" : "7",
  "name" : "Erd"
 }
]'''

info = json.loads(data)
print('User Count:', len(info))

for item in info:
    print("Name: ", item['name'])
    print("ID: ", item['id'])
    print("Attribute: ", item['x'])