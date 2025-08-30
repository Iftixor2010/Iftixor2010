import json
bemor = {
    "ism": "alijon g'aniyev",
    "yosh": 30,
    "oila": True,
    "farzandlar": ("ahmat","bonu"),
    "allergiya": None,
    "dorilar":[
        {"nomi": "analgin", "miqdori": 0.5},
        {"nomi": "panadol", "miqdori": 1.2}
    ]
}

with open('bemor.json', 'w') as f:
    bemor_json=json.dump(bemor,f)

print(bemor_json)