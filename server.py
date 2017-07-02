from flask import Flask, render_template, jsonify
import calendar
import json
import const

from apiclient.discovery import build

app = Flask(__name__)

@app.route('/', methods=['GET'])
def initialize ():
    return render_template('index.html')

def getRunningData (monthNum):
    month = calendar.month_name[monthNum]
    lastDayRow = calendar.monthrange(2017, monthNum)[1] + 1
    query = month + '!A2:B' + str(lastDayRow)

    service = build('sheets', 'v4', developerKey = const.DEVELOPER_KEY)
    request = service.spreadsheets().values().get(spreadsheetId = const.SPREADSHEET_ID, range=query)
    response = request.execute()
    return response

@app.route('/month/<int:month>', methods=['GET'])
def runningData (month):
    data = getRunningData(month)
    ret = [formatObject(x) for x in data['values']]
    return json.dumps(ret)

# Format response as array of objects:
#   {
#       'date': mm/dd/yyyy,
#       'distance': int
#   }
def formatObject (entry):
    obj = {}
    obj['date'] = entry[0]
    obj['distance'] = entry[1]
    return obj
