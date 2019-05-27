import yaml

data = {'info': {'data001': {'name': 'bob'},
                 'data002': {'age': 19},
                 'address': '航都路18号'},
        'data': {'data001': {'name': 'bob'},
                 'data002': {'age': 19},
                 'address': '航都路18号',
                 'name': 'bob',
                 'age': 19,
                 'hobby': 'sing'}}

with open("./wdata.yaml", "a", encoding="utf-8") as f:
    yaml.safe_dump(data, f, encoding="utf-8", allow_unicode=True)
