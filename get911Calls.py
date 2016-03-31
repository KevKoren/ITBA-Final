import datetime, time, random
from urllib import request

def query911API(fromDate, toDate):
    return request.urlopen('http://bahiablanca.gov.ar:8080/Publico/qpbb?'
        'f1=' + fromDate.strftime('%d/%m/%Y') + ''
        '&f2=' + toDate.strftime('%d/%m/%Y')).read().decode('utf-8')


if __name__ == '__main__':
    queryDate = datetime.datetime(2009, 8, 6)
    strLastDate = datetime.datetime.today().strftime('%Y%m%d')

    startTime = time.time()

    while queryDate.strftime('%Y%m%d') <= strLastDate:
        destPath = './data/911Calls/' + queryDate.strftime('%Y%m%d') + ' - 911 Calls.xml'
        destFile = open(destPath, 'w', encoding='utf-8')
        destFile.write(query911API(queryDate, queryDate))
        destFile.close()

        print(queryDate.strftime('%Y%m%d'))
        print("Elapsed %d: " % int(time.time() - startTime))

        queryDate += datetime.timedelta(days=1)
        time.sleep(random.randint(0, 3))

