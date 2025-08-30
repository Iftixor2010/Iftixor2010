import json
filename='bemor.json'
with open(filename) as f:
    bemor=json.load

print(type(bemor))