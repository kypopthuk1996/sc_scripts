from __future__ import print_function
import pickle
import os.path
from pprint import pprint
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from add_object_to_gsheets import loadjson, parse_json

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1cqJVtaHWTozVZFdKBBUNwCqET63aY9JZVgXRuqwT_aA'
SAMPLE_RANGE_NAME = 'SIP!B1:B3'
CREDENTIALS_FILE = 'creds.json'
pathJsonScript = '/Users/dmitrijminor/tests'

def glav():
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

def show_sheets(obj):
    # Call the Sheets API
    result = obj.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                        range=SAMPLE_RANGE_NAME, majorDimension='ROWS').execute()
    values = result.get('values', [])
    pprint(values)

def add_sheets(obj, prs_val, m):
    # Add to Sheets new value
    result = obj.spreadsheets().values().batchUpdate(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": f"SIP!A313:I{m}",
                 "majorDimension": "ROWS",
                 "values": prs_val}
            ]
        }
    ).execute()

service = glav()
show_sheets(service)
listpath = loadjson(pathJsonScript)
add_sheets(service, parse_json(listpath), 1301)
