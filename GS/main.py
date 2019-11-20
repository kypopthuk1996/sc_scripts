import sys
from modules.work_gsheets import main_fun, show_sheets
from modules.add_object_to_gsheets import *
from modules.parser_gs import *
MAIN_SPREADSHEET_ID = '1cqJVtaHWTozVZFdKBBUNwCqET63aY9JZVgXRuqwT_aA'
pathJsonScript = '/Users/dmitrijminor/tests/cdr'
SAMPLE_RANGE_NAME = 'Main!103:110'
HEADER = 'Main!1:1'

data_sheet = show_sheets(main_fun(),MAIN_SPREADSHEET_ID,SAMPLE_RANGE_NAME)
listpath = (loadjson(pathJsonScript))
header_sheet = show_sheets(main_fun(),MAIN_SPREADSHEET_ID,HEADER)
#print(data_sheet)
#print(parse_json(listpath)[2])
#print(search_tag())
#print(data_sheet[0]
pars = Parser()
key_colunns_dict = pars.pars_key_columns(header_sheet)
print(key_colunns_dict)
print('-'*100)

for str_data in data_sheet[0:]:
    print(pars.parsing_in_parts(str_data, key_colunns_dict))

#print('-'*100)
#print(pars.main_parts.table_assembly())