import json
x=10
x_json=json.dumps(x)
ism="anvar"
ism_json=json.dumps(ism)
sonlar=[12,45,23,67]
sonlar_json=json.dumps(sonlar)
print(x_json)
print(ism_json)
print(sonlar_json)
sonlar=json.loads(sonlar_json)
