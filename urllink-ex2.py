import urllib.request
from bs4 import BeautifulSoup
import ssl
import re

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position:'))


for i in range(count):
#anchor 태그 찾기
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print("Retrieving: ", url)
    tags = soup('a')
    link = (tags[position-1].get('href', None))
    url = link
    if i == count-1:
        name = tags[int(position)-1].text

print("Retrieving: ", url)
print('Name',name)



# http://py4e-data.dr-chuck.net/known_by_Fikret.html
