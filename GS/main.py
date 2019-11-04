import sys
from modules.work_gsheets import main_fun, show_sheets
from modules.add_object_to_gsheets import *

pathJsonScript = '/Users/dmitrijminor/tests/cdr'

data_sheet = show_sheets(main_fun(),'SIP!A:I')
listpath = (loadjson(pathJsonScript))
#print(parse_json(listpath)[2])
print(search_tag())
