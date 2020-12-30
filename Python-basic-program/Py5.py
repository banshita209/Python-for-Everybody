import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter - ')
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
print('count :', len(lst))
sum=0
for item in lst:
    #print('name :', item.find('name').text)
    #print('no :', item.find('count').text)
    no=item.find('count').text
    sum=sum+int(no)
print('sum :',sum)
