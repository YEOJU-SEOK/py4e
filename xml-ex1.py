import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#sample http://py4e-data.dr-chuck.net/comments_42.xml
#test  http://py4e-data.dr-chuck.net/comments_1512232.xml

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)

data = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

counts = tree.findall('.//count')
print(f"Count: {len(counts)}")

count_list = list()

for item in counts:
    num = int(item.text)
    count_list.append(num)

print(f"Sum: {sum(count_list)}")
