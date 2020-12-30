import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
count = input('Enter count-')
pos = input('Enter position -')
count=int(count)
pos=int(pos)
print(count, '- ',pos)
i_pos: int = 1
j_count = 0
name = ""
while j_count!=count:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print(url)
    for tag in tags:
        if i_pos==pos:
            url = tag.get('href', None)
            name=tag.contents[0]

            j_count += 1
            i_pos=1
            break
        else:
            i_pos += 1
print(url)
print(name)