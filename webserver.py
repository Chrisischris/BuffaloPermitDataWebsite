from bottle import route, run, template, SimpleTemplate, static_file
import json, os, urllib.request
import csv, filterData

allData = []

def loadData(filenameRoot, howMany):
    csvFile = filenameRoot
    if not os.path.isfile(csvFile):
        params = urllib.parse.urlencode({"$limit": howMany})
        uri = "https://data.buffalony.gov/resource/9p2d-f3yt.json?%s" % params
        response = urllib.request.urlopen(uri)
        content_string = response.read().decode()
        content = json.loads(content_string)
        csv.writeDataToCSVFile(csvFile, content, ['apno', 'aptype', 'issued', 'value'], True)

@route('/')
def index():
    return static_file('index.html', root='')


@route('/script.js')
def js():
    return static_file('script.js', root='')


@route('/barJSON')
def barJSON():
    data = []
    d = {"x": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], "y": [], "type": "bar"}

    for m in range(1,13):
        res = filterData.filterByMonth(allData, m)
        d.get("y").append(len(res))

    data.append(d)
    return json.dumps(data)


@route('/lineJSON')
def lineJSON():
    data = []
    d = {"x": [], "y": [], "mode": "lines", "type":"scatter"}

    for y in range(2008,2020):
        d.get("x").append(y)
        res = filterData.filterByYear(allData, y)
        d.get("y").append(len(res))

    data.append(d)
    return json.dumps(data)


@route('/scatterJSON')
def scatterJSON():
    data = []

    for y in range(2008,2020):
        d = {"x": [], "y": ["Small", "Medium", "Large"], "name": y, "mode": "markers", "type":"scatter", "marker":{"size": 12 }}
        res = filterData.filterByYear(allData, y)
        small = filterData.filterInRange(res, " value", 0, 5000)
        medium = filterData.filterInRange(res, " value", 5000, 50000)
        large = filterData.filterInRange(res, " value", 50000, 500000)

        sV = 0
        for v in small:
            sV += int(float(v.get(" value")))
        d.get("x").append(sV)

        mV = 0
        for v in medium:
            mV += int(float(v.get(" value")))
        d.get("x").append(mV)

        lV = 0
        for v in large:
            lV += int(float(v.get(" value")))
        d.get("x").append(lV)
        data.append(d)
        

    return json.dumps(data)


loadData("permitData.csv", 5000)
allData = csv.readDataFromCSVFile("permitData.csv")
run(host='localhost', port=8080)
