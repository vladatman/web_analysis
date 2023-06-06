from google.oauth2 import service_account
from googleapiclient.discovery import build

CREDENTIALS_FILE = 'C:/credentials.json'

VIEW_ID = 'YOUR_VIEW_ID'

# Створюємо сервіс Google Analytics
credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE)
service = build('analyticsreporting', 'v4', credentials=credentials)

response = service.reports().batchGet(
    body={
        'reportRequests': [
            {
                'viewId': VIEW_ID,
                'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:sessions'}, {'expression': 'ga:newUsers'}, {'expression': 'ga:sessionDuration'}],
                'dimensions': [{'name': 'ga:date'}]
            }]
    }
).execute()

for report in response.get('reports', []):
    rows = report.get('data', {}).get('rows', [])
    for row in rows:
        date = row['dimensions'][0]
        sessions = row['metrics'][0]['values'][0]
        new_users = row['metrics'][0]['values'][1]
        session_duration = row['metrics'][0]['values'][2]
        print(f"Date: {date}, Sessions: {sessions}, New Users: {new_users}, Session Duration: {session_duration}")
