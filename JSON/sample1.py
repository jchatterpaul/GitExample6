import json
from pprint import pprint

stream = open('sample1.json','r')
jsonobj = json.load(stream)
pprint(type(jsonobj))

print(jsonobj['People'][2]['Email'])
###############################################################

# stream2 = """{"People": 
#     [
#         {
#             "Id": "1",
#             "FirstName": "Benjamin",
#             "LastName": "Finkel",
#             "Email": "ben.finkel@cbtnuggets.com"
#         },
#         {
#             "Id": "2",
#             "FirstName": "Jane",
#             "LastName": "Doe",
#             "Email": "jane.doe@cbtnuggets.com"
#         },
#         {
#             "Id": "3",
#             "FirstName": "Pat",
#             "LastName": "Smith",
#             "Email": "pat.smith@cbtnuggets.com"
#         }
#     ]
# }
# """
# jsonobj2 = json.loads(stream2)
# pprint(type(jsonobj2))