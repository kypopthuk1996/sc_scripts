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
    '''
    Главная функция, которая произвродит аутентификациб в таблицах
    :return:
    '''
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service_auth = build('sheets', 'v4', http=httpAuth)
    return service_auth

def show_sheets(obj, sps_id ,range):
    '''
    Фунция считывает строки из таблицы
    :param obj: вызывает результат main_fun
    :param sps_id: ID таблицы, которую нужно читать
    :param range: Диапозон в котором производится считывание
    :return: возвращает список из списков. Где каждый список это строка таблицы
    '''
    result = obj.spreadsheets().values().get(spreadsheetId=sps_id,
                        range=range, majorDimension='ROWS').execute()
    values = result.get('values', [])
    return values

def add_sheets(obj, sps_id, prs_val, start_pos, fin_pos):
    '''
    Функция добавляет в таблицу новые значения
    :param obj: вызывает результат main_fun
    :param sps_id: ID таблицы, которую нужно читать
    :param prs_val: Список с добавляемыми значениями
    :param start_pos: Стартовая строка
    :param fin_pos: Последняя строка
    :return:
    '''
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
    '''
    Фунция очищает таблицу в заданном диапозоне
    :param obj: вызывает результат main_fun
    :param start_pos: Стартовая строка
    :param fin_pos: Последняя строка
    :return:
    '''
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
    '''
    Функция копирует одну таблицу в другую
    :param obj: вызывает результат main_fun
    :param COPY_SPREADSHEET_ID:  ID новой таблицы
    :param sheet_id: ID страницы, которую стоит копировать
    :return:
    '''
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
