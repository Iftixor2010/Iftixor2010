import json
x=10
x_json=json.dumps(x)
print(type(x_json))
print(x_json)

y=5.5
y_json=json.dumps(y)
print(type(y_json))
print(y_json)

m=True
m_json=json.dumps(m)
print(type(m_json))
print(m_json)
print(json.loads(m_json))


sonlar=(12, 45, 23, 67)
sonlar_json=json.dumps(sonlar)
print(type(sonlar))
print(sonlar_json)
print(json.loads(sonlar_json))