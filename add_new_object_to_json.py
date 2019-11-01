#!/usr/bin/python3
import os
import json

#This script allows the substitution of new object ​​in the current JSON files

pathJsonScript = '/home/dima/Work/test/ss_cfu' #Path to JSON Files
res = 0

#Function overwriting JSON files with new values
def add_key(new_key, new_value, last_key, old_dict):
    new_dict = dict() #Create new dictionary
    for value in old_dict: #old dictionary pass
        new_dict[value] = old_dict[value] #rewrite new dictionary
        if value == last_key: #Condition - if you find a key after which to record, then assign a new value
            new_dict[new_key] = new_value #assign a new value
    return new_dict #return new dictionary

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

listpath = loadjson(pathJsonScript) #Start the function loadjson and assign its value to a variable listpath
new_key = input('Введите новый ключ (Пример: Tag): ')
new_value = input('Введите значение данного ключа (Пример: [\'ssw\', \'ecss3.11\']): ')
last_key = input('Введите ключ после которого вставить новый ключ (Пример: Users): ')
for list1 in listpath: #iterate over all the JSON files
        with open(list1, 'r') as j_file: #open file for read
            data = json.load(j_file) #read data in JSON file
        with open(list1, 'w') as j_file: #open file for write
            data = json.dumps(add_key(new_key, new_value, last_key, data), ensure_ascii=False, indent=2) #rewrite data
            j_file.write(data) #write new data in JSON file
        pass
