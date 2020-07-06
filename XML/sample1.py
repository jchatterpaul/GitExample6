# #import xml.etree.ElementTree as ET
# from lxml import etree as ET

# stream = open('sample1.xml','r')

# # Parse the data into an ElementTree object
# xml = ET.parse(stream)

# # Get the root element object from the ElementTree
# rootelement = xml.getroot()

# for root in rootelement:
#     print(ET.tostring(root)) 
#     #print("**")
#     print(root.get("Id"))

#####################################################################

import xmltodict
from pprint import pprint

stream = open('sample1.xml','r')

# Parse the XML file into an OrderedDict
xml = xmltodict.parse(stream.read())

for item in xml:
    print(item)
    
for item in xml['People']:
    print(item)

for item in xml['People']['Person']:
    pprint(item)


