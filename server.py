from flask import Flask, render_template, jsonify, request, make_response, Response
import calendar
import json
import const

from apiclient.discovery import build

app = Flask(__name__)
bookInfo = []

@app.route('/', methods=['GET'])
def initialize ():
    return render_template('index.html')

@app.route('/month/<int:month>', methods=['GET'])
def runningData (month):
    data = getRunningData(month)
    ret = [formatRunningObject(x) for x in data['values']]
    return json.dumps(ret)

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
    # resp = make_response(json.dumps(bookInfo))
    resp = jsonify(bookInfo)
    #resp = Response(resp1, status=200, mimetype='application/json')
    #resp.body = resp1
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    return resp1

def buildBookList (request_id, response, exception):
    global bookInfo
    return bookInfo.append(response)

def getRunningData (monthNum):
    month = calendar.month_name[monthNum]
    lastDayRow = calendar.monthrange(2017, monthNum)[1] + 1
    query = month + '!A2:B' + str(lastDayRow)

    service = build('sheets', 'v4', developerKey = const.DEVELOPER_KEY)
    request = service.spreadsheets().values().get(spreadsheetId = const.SPREADSHEET_ID, range=query)
    response = request.execute()
    return response

# Format response as array of objects:
#   {
#       'date': mm/dd/yyyy,
#       'distance': int
#   }
def formatRunningObject (entry):
    obj = {}
    obj['date'] = entry[0]
    obj['distance'] = entry[1]
    return obj
