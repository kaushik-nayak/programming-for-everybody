import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json
url=input("enter :")
data=urllib.request.urlopen(url).read()
xmldata=ET.fromstring(data)
searchstr="comments/comment"
counttags=xmldata.findall(searchstr)

total=0
for tags in counttags:
    c=tags.find('count')
    total=total+int(c.text)
print(total)
