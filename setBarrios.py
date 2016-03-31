import csv, xml.dom.minidom as minidom

def point_inside_polygon(x,y,poly):

    n = len(poly)
    inside =False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside


barrioKMLPath = 'Tableau/barrios/Barrios_Oficiales.kml'

dom = minidom.parse(barrioKMLPath)

barriosPolygons = {}

for barrio in dom.getElementsByTagName('Placemark'):
    nombre = barrio.getElementsByTagName('name')[0].childNodes[0].data.strip()
    coordinates = barrio.getElementsByTagName('coordinates')[0].childNodes[0].data.strip().replace('0.000000 ', '').replace('0.000000', '').split(',')
    poly = [(float(x),float(y)) for x,y in zip(coordinates[0::2], coordinates[1::2])]
    barriosPolygons[nombre] = poly


def getBarrio(lat, lon):
    for barrio, poly in barriosPolygons.items():
        if point_inside_polygon(lon, lat, poly):
            return barrio
    return ""

srcPath = 'data/911Calls/20070528 a 20160304 - 911 Calls.tsv'
dstPath = 'data/911Calls/20070528 a 20160304 - 911 Calls with Barrios.tsv'

srcFile = open(srcPath, 'r', encoding='utf-8')
dstFile = open(dstPath, 'w', encoding='utf-8')
reader = csv.reader(srcFile, delimiter="\t")
writer = csv.writer(dstFile, delimiter="\t", lineterminator="\n")

current = reader.__next__()
current.append('barrio')
del current[4]
writer.writerow(current)
try:
    while current:
        current = reader.__next__()
        current.append(getBarrio(float(current[5].replace(',', '.')), float(current[6].replace(',', '.'))))
        del current[4]
        writer.writerow(current)
except StopIteration:
    pass

srcFile.close()
dstFile.close()

