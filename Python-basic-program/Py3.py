import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input('Enter-')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

tags=soup('span')
count=0
sum=0
for tag in tags:
   count=count+1
   sum=sum+int(tag.contents[0])
  # print('TAG:', tag)
   #print('URL:', tag.get('td', None))
   #print('Contents:', tag.contents[0])
  # str=tag.contents[0]
   #print(str.findall([0-9]))
   #print('Attrs:', tag.attrs)
print('Count',count)
print('Sum',sum)
