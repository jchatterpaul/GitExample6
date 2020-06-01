import xmltodict

# get the xml file data
stream = open('xml.xml','r')

# parse the xml file into an orderdict
xml = xmltodict.parse(stream.read())

for e in xml:
    print(e)

for e in xml['catalog']:
    print(e)

for e in xml['catalog']['book']:
    print(e)