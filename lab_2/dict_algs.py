ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    },{
        "name": "petja",
        "age": 19,
    }],
}

darja = {
    "name": "darja",
    "age": 41,
    "children" : [{
        "name" : "kirill",
        "age": 21,
    },{
        "name" : "pavel",
        "age" : 19,
    }],
}

def children (masd):
    mas = []
    for dic in  masd:
        for child in dic ['children']:
            if child ['age'] > 18:
                mas. append (dic ['name'])
                break
    return mas

emp = [ivan, darja]
print(children(emp))