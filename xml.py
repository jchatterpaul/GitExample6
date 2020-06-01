from lxml import etree as ET

# get the xml file data
stream = open('sample.xml','r')

# parse the data into an ElementTree object
xml = ET.parse(stream)

# get the root element object from the ElementTree
root = xml.getroot()

# iterate through each child of the root element
for e in root:
    # print the stringified version of the element
    print(ET.tostring(e))
    print("")

    # print the ID attribute of the element object
    print(e.get("id"))