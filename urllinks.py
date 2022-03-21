import urllib.request
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('enter-')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#anchor 태그 찾기
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))


#http://www.dr-chuck.com/page1.htm
#http://www.dr-chuck.com/page2.htm
