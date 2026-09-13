
# JSON has no end tag, no start tag, and no attributes
import json
data = '''
{
    "name": "chuck",
    "phone": {
        "type": "int1",
        "number": "+1 734 303 4456"
    },
    "email": {
        "hide": "yes"
    }
}
'''
info = json.loads(data)
print(info["name"])
print(info["email"]["hide"]) 