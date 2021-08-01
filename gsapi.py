from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# read_data - data reading function
def read_data(spreadsheet_id, sheet_range):   
    
    result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                range=sheet_range).execute()
    values = result.get('values', [])
    return values


# push_data - data exporting function
def push_data(spreadsheet_id, sheet_range, data):
    result = sheet.values().update(spreadsheetId=spreadsheet_id,
                                range=sheet_range, valueInputOption='USER_ENTERED',
                                body={"values":data}).execute()