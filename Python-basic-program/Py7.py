import json
import urllib.request, urllib.parse, urllib.error


url=input('Enter -')
content = urllib.request.urlopen(url)
data=content.read().decode()
info = json.loads(data)
print('User count:', len(info['comments']))
sum=0
for item in info['comments']:
    #print('Name', item['name'])
    #print('count', item['count'])
    sum=sum+item['count']
print('Sum :',sum)