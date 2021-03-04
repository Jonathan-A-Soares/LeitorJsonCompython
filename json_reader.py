import json

with open('daos.json') as f:    
    data = json.load(f)
print (data['some'])
