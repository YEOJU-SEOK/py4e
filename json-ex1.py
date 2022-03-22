#sample http://py4e-data.dr-chuck.net/comments_42.json
#test http://py4e-data.dr-chuck.net/comments_1512233.json

import urllib.request
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)

data = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
comments = info['comments']

print(f"Count : {len(comments)}")

result = 0
for comment in comments:
    result += int(comment['count'])

print(f"Sum : {result}")
