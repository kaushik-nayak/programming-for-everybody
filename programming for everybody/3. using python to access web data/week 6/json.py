import urllib.request, urllib.parse, urllib.error
import ssl
import json
url=input("enter")
dat=urllib.request.urlopen(url).read()
data=json.loads(dat)


total=0
for tags in data['comments']:

    total=total+tags["count"]
print(total)
