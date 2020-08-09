import gspread
from oauth2client.service_account import ServiceAccountCredentials

class SpreadSheet:

    def __init__(self, name):
        scope = ['https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(credentials)
        self.sheet = client.open(name).sheet1

    def insert_record(self, row, index):
        self.sheet.insert_row(row, index)

    def get_all_record(self):
        return self.sheet.get_all_records()
