import json
import re
import csv

with open('tweet_refugee.json', 'r') as handle:
    text_data = handle.read()
    text_data = '[' + re.sub(r'\}\s\{', '},{', text_data) + ']'
    json_data = json.loads(text_data)

#print(json_data[0]['text'])

for i in range(len(json_data)):
    print(json_data[i]['text'])

'''
data = json.load(json_data)
f.close()
f = open('data.csv')
print(data)
csv_file = csv.writer(f)
for item in data:
    f.writerow(item)

f.close()
'''
