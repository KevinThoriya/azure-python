from get_azure_Data import AzureData
from google_sheet import SpreadSheet
from settings import settings
# print( settings)
import schedule
import time

azure_connect = AzureData(settings.get('Azure Url'), settings.get('Auth Token'), settings.get('project'))
google_sheet_connect = SpreadSheet(settings.get('google sheet name'))
row_init = ['ID', 'Type', 'State', 'Assign', 'Create Date', 'State Change Date', 'Title']
google_sheet_connect.insert_record(row_init, 1)


def get_azure_and_store_sheet():
    rows = azure_connect.get_close_workitem()
    # print(rows)
    for row in rows:
        # print('add')
        google_sheet_connect.insert_record(row, 2)

# get_azure_and_store_sheet()


schedule.every().day.at("23:59").do(get_azure_and_store_sheet)

while True:
    schedule.run_pending()
    time.sleep(1)