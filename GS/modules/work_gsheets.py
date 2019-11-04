from __future__ import print_function
from pprint import pprint
from googleapiclient.discovery import build
import httplib2
import logging
from oauth2client.service_account import ServiceAccountCredentials
import sys
sys.path.append('../')

# The ID and range of a sample spreadsheet.
MAIN_SPREADSHEET_ID = '1cqJVtaHWTozVZFdKBBUNwCqET63aY9JZVgXRuqwT_aA'
COPY_SPREADSHEET_ID = '12MakhxCjL2Tg90vn5e1fqHdRzRJ9qvy4hbHV6nQ09cU'
SAMPLE_RANGE_NAME = 'SIP!B1:B3'
SHEET_ID = '906508873'
CREDENTIALS_FILE = 'creds.json'
pathJsonScript = '/Users/dmitrijminor/tests/cdr'
TEST_RANGE = 'SIP!A313:I1299'
START_POS = 3
def main_fun():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service_auth = build('sheets', 'v4', http=httpAuth)
    return service_auth

def show_sheets(obj, range):
    # Call the Sheets API
    result = obj.spreadsheets().values().get(spreadsheetId=MAIN_SPREADSHEET_ID,
                        range=range, majorDimension='ROWS').execute()
    values = result.get('values', [])
    return values

def add_sheets(obj, sps_id, prs_val, start_pos, fin_pos):
    # Add to Sheets new value
    result = obj.spreadsheets().values().batchUpdate(
        spreadsheetId=sps_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": f"ДВО!A{start_pos}:I{start_pos+fin_pos}",
                 "majorDimension": "ROWS",
                 "values": prs_val}
            ]
        }
    ).execute()

def clear_list(obj, start_pos, fin_pos):
    body_clear_list = {
        "requests": [
            {
                "deleteDimension": {
                    "range": {
                        "sheetId": SHEET_ID,
                        "dimension": "ROWS",
                        "startIndex": start_pos-1,
                        "endIndex": start_pos+fin_pos
                    }
                }
            },
        ],
    }
    result = obj.spreadsheets().batchUpdate(
        spreadsheetId=MAIN_SPREADSHEET_ID,
        body=body_clear_list
    ).execute()

def copy_sheets(obj,COPY_SPREADSHEET_ID,sheet_id):
    body_copy_sheets = {
    'destination_spreadsheet_id': COPY_SPREADSHEET_ID,
    }
    result = obj.spreadsheets().sheets().copyTo(
        spreadsheetId=MAIN_SPREADSHEET_ID,
        sheetId=sheet_id,
        body=body_copy_sheets
    ).execute()

if __name__ == '__main__':
    service = main_fun()
    listpath = loadjson(pathJsonScript)
    res_pars = parse_json(listpath)
    add_sheets(service, COPY_SPREADSHEET_ID, res_pars[0], START_POS , res_pars[1])
    #show_sheets(service, TEST_RANGE)
    #clear_list(service, START_POS, res_pars[1])
    #copy_sheets(service, COPY_SPREADSHEET_ID, SHEET_ID)
