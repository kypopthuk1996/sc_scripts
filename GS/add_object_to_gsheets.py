import os
import json
pathJsonScript = '/Users/dmitrijminor/tests'
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
    m = -1
    for f1 in file:
        with open(f1, 'r') as f:
            data = json.load(f)
        g = data.get('Tests', '')
        for a in g:
            new_dict.append(['', data.get('TestName', ''), a.get('Name', ''), a.get('Description', ''), 'Succ', '', '', 'auto', 'sip'])
            m += 1
    return new_dict, m


if __name__ == '__main__':
    listpath = loadjson(pathJsonScript)
    #print('\n'.join(listpath))
    fin = parse_json(listpath)
    print(fin[1])
