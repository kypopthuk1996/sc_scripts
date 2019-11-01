import add_object_to_gsheets
import os
import json

class Parser():
    def __init__(self):
        pass

    def Loadjson(path):
        m = 0
        res = []  # Create empty dictionary
        with os.scandir(path) as it:  # scan path to JSON file
            for entry in it:
                if entry.is_file():
                    if '.json' in entry.name:  # if a JSON file is found, then write it to the res list
                        res.append(path + '/' + entry.name)
                else:
                    res.extend(Parser.Loadjson(path + '/' + entry.name))  # if a JSON file is not found, then go down one folder
        return res

    def Parse_json(file):
        new_dict = []
        for f1 in file:
            print(f1)
            with open(f1, 'r') as f:
                data = json.load(f)
            g = data.get('Tests', '')
            for a in g:
                new_dict.append(
                    ['', data.get('TestName', ''), a.get('Name', ''), a.get('Description', ''), '', '', 'auto'])
        print(new_dict)
        return new_dict