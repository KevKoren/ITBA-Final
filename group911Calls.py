import datetime

destPath = './data/911Calls/20070528 a 20160304 - 911 Calls.xml'

destFile = open (destPath, 'w', encoding='utf-8');

startDate = datetime.datetime(2007,5,28)
endDate = datetime.datetime(2016,3,4)
currentDate = startDate
i = 0
while currentDate <= endDate:
    with open('./data/911Calls/' + currentDate.strftime('%Y%m%d') + ' - 911 Calls.xml','r', encoding='utf-8') as inputFile:
        inputFile.readline()
        inputFile.readline()
        inputFile.readline()
        line = inputFile.readline()
        while line:
            if not (line == '</items>' or line ==''):
                destFile.write(line)
            line = inputFile.readline()
    i += 1
    print(i)
    currentDate += datetime.timedelta(days=1)
destFile.close()