import os
import json

pathJsonScript = '/home/dima/Work/test'
res = 0

def loadjson(path):
    m = 0
    res = [] #Create empty dictionary
    with os.scandir(path) as it: #scan path to JSON file
        for entry in it:
            if entry.is_file():
                if '.json' in entry.name: #if a JSON file is found, then write it to the res list
                    res.append(path + '/' + entry.name)
            else:
                res.extend(loadjson(path + '/' + entry.name)) #if a JSON file is not found, then go down one folder
    return res

def parse_json(file):
    new_dict = {}
    for f1 in file:
        print(f1)
        with open(f1, 'r') as f:
            data = json.load(f)
        new_dict[data.get('TestName', '')] = {}
        g = data.get('Tests', '')
        for a in g:
            new_dict[data.get('TestName', '')][a.get('Name', '')] = a.get('Description', '')
    print(new_dict)


listpath = loadjson(pathJsonScript)
#print('\n'.join(listpath))
fin = parse_json(listpath)