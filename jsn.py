import json

stream = open('sample.json','r')

jsonobj = json.load(stream)

print(jsonobj)