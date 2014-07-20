
import json
from pprint import pprint
data = open("c:\users\sentiking\desktop\json.txt").read()
s=json.dumps(data,indent= 4,sort_keys=True)
d=json.loads(data)
pprint (d)
for x in d['value']['items']:
    print x['title']
