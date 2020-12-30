import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

count=dict()
for fline in fhand:
    words=fline.decode().split()
    for word in words :
        count[word]=count.get(word,0)+1
print(count)


