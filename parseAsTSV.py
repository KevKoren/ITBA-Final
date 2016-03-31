import datetime, csv, xml.dom.minidom as minidom


srcPath = './data/911Calls/20070528 a 20160304 - 911 Calls.xml'
#srcPath = './data/911Calls/20070528 - 911 Calls.xml'
destPath = './data/911Calls/20070528 a 20160304 - 911 Calls.tsv'


destFile = open (destPath, 'w', encoding='utf-8');
writer = csv.writer(destFile, lineterminator='\n', delimiter='\t')

writer.writerow(['fecha', 'hora', 'evento', 'domicilio', 'localidad', 'lat', 'lng'])

i= 0

dom = minidom.parse(srcPath)

print("Parse dom ended, starting to write output")

for item in dom.getElementsByTagName('item'):
    fecha = item.getElementsByTagName('fecha')[0].childNodes[0].data.strip()[0:10]
    hora = item.getElementsByTagName('fecha')[0].childNodes[0].data.strip()[11:]
    evento = item.getElementsByTagName('evento')[0].childNodes[0].data.strip()
    domicilio = item.getElementsByTagName('domicilio')[0].childNodes[0].data.strip()
    localidad = item.getElementsByTagName('localidad')[0].childNodes[0].data.strip()
    lat = item.getElementsByTagName('lat')[0].childNodes[0].data#.replace(',', '.').strip()
    lng = item.getElementsByTagName('lng')[0].childNodes[0].data#.replace(',', '.').strip()

    row = [fecha, hora, evento, domicilio, lat,lng]
    writer.writerow(row)

    i += 1
    if i % 1000 == 0:
        print(i)

destFile.close()
