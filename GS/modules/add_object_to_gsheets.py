import os
import json
import sys
sys.path.append('../')
pathJsonScript = '/Users/dmitrijminor/tests/cdr'
res = 0


def loadjson(path):
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
    new_dict = []
    tag_dict = []
    m = -1
    for f1 in file:
        with open(f1, 'r') as f:
            data = json.load(f)
        g = data.get('Tests', '')
        tag_dict.append(data.get('Tag', ''))
        new_dict.append(['', data.get('Topic', ''), '', data.get('Description', ''), 'Succ'])
        m += 1
        for a in g:
            new_dict.append(['', data.get('TestName', ''), a.get('Name', ''), a.get('Description', ''), 'Succ', 'auto'])
            m += 1
    return new_dict, m, tag_dict

def search_tag(data_sheet):
    path_list = loadjson(pathJsonScript)
    tag = parse_json(path_list)[2]
    for str_sheet in data_sheet:
        for list_tag in tag:
            for val_tag in list_tag:
                if val_tag == str_sheet[8]:
                    continue



    print(result)

