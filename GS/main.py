import sys
from modules.work_gsheets import main_fun, show_sheets
from modules.add_object_to_gsheets import *
from modules.parser_gs import *
MAIN_SPREADSHEET_ID = '1cqJVtaHWTozVZFdKBBUNwCqET63aY9JZVgXRuqwT_aA'
pathJsonScript = '/Users/dmitrijminor/tests/cdr'
SAMPLE_RANGE_NAME = 'SIP!210:222'

data_sheet = show_sheets(main_fun(),MAIN_SPREADSHEET_ID,SAMPLE_RANGE_NAME)
listpath = (loadjson(pathJsonScript))
#print(data_sheet)
#print(parse_json(listpath)[2])
#print(search_tag())

for str_data in data_sheet:
    pars = Parser().pars_gs(str_data)
    print(pars)