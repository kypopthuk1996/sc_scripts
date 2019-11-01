from pprint import pprint
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import httplib2
from oauth2client.service_account import ServiceAccountCredentials


# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1cqJVtaHWTozVZFdKBBUNwCqET63aY9JZVgXRuqwT_aA'
sheet_id = '906508873'
# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = build('sheets', 'v4', http = httpAuth)

"""Копирую шитс в новый спредшитс
copy_sheet_to_another_spreadsheet_request_body = {
    # The ID of the spreadsheet to copy the sheet to.
    'destination_spreadsheet_id': '1HZx63Q9ErYmQBeEuAmYQjroFFg2x_nnFCF795EdSOWM',
}

request = service.spreadsheets().sheets().copyTo(spreadsheetId=spreadsheet_id, sheetId=sheet_id, body=copy_sheet_to_another_spreadsheet_request_body)
response = request.execute()
pprint(response)
"""
include_grid_data = False
# Пример чтения файла
values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='Лист3!A1:E200',
    majorDimension='COLUMNS'
).execute()

#gg = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges='A1:E10', includeGridData=include_grid_data).execute()
pprint(values)
#pprint(gg)


# Пример записи в файл
'''values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист3!B3:C4",
             "majorDimension": "ROWS",
             "values": [["This is B3", '', "This is C3"], ["This is B4", "This is C4"]]},
            {"range": "Лист3!D5:E6",
             "majorDimension": "COLUMNS",
             "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
	]
    }
).execute()
'''