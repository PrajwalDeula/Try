import json

x = {
    "name": "Xyz",
    "gender" : "male",
    "married": True,
    "divorce": False,
    "pet": None,
    "children": ("Randy","Orton"),
    "car":[
        {"model":"BMW","mpg":23},{"model":"Aston Martin","mpg":22}
    ]
}

print(json.dumps(x,indent=4,separators= ("."," = ")))