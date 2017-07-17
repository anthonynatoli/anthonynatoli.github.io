import calendar
import datetime
import json
from flask import Flask, render_template, jsonify, request, make_response
import const

from apiclient.discovery import build

app = Flask(__name__)
bookInfo = []

@app.route('/', methods=['GET'])
def initialize ():
    return render_template('index.html')

@app.route('/run', methods=['GET'])
def runningData ():
    month = int(datetime.datetime.now().strftime("%m"))
    data = [getRunningData(i) for i in range(1, month + 1)]

    ret = {}
    for x in range(len(data)):
        ret[str(x)] = []
    [ret[str(x)].append(formatRunningObject(y)) for x in range(len(data)) for y in data[x]['values']]

    response = jsonify(ret)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

@app.route('/books', methods=['GET'])
def books ():
    book_ids = ['diAFQgAACAAJ', # Devil in the White City
    'yxv1LK5gyV4C', # 1984
    'pWAYDQAAQBAJ', # Good Clean Fun
    '4rXJDAEACAAJ', # Norse Mythology
    'xpJHDAAAQBAJ', # The Undoing Project
    '2NIpDAAAQBAJ', # The Martian
    'ekWLDQAAQBAJ' # The Signal and the Noise
    ]

    service = build('books', 'v1', developerKey = const.DEVELOPER_KEY)
    global bookInfo
    bookInfo = []
    
    batch = service.new_batch_http_request(callback = buildBookList)
    [batch.add(service.volumes().get(volumeId = book_ids[x])) for x in range(len(book_ids))]
    response = batch.execute()

    resp = jsonify(bookInfo)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    return resp

def buildBookList (request_id, response, exception):
    global bookInfo
    return bookInfo.append(response)

def getRunningData (monthNum):
    month = calendar.month_name[monthNum]
    lastDayRow = calendar.monthrange(2017, monthNum)[1] + 1
    query = month + '!A2:C' + str(lastDayRow)

    service = build('sheets', 'v4', developerKey = const.DEVELOPER_KEY)
    run_request = service.spreadsheets().values().get(spreadsheetId = const.SPREADSHEET_ID, range=query)
    response = run_request.execute()
    return response

# Format response as array of objects:
#   {
#       'date': mm/dd/yyyy,
#       'distance': int
#   }
def formatRunningObject (entry):
    obj = {}
    obj['date'] = entry[0]
    if len(entry) > 1:
        obj['distance'] = entry[1]

        if len(entry) > 2 and float(obj['distance']) > 0:
            obj['activity'] = entry[2]
        else:
            obj['activity'] = 'run'
    return obj
