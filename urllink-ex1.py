# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
s = 0
count = 0
for tag in tags:
    # Look at the parts of a tag
    content = int(tag.contents[0])
    s += content
    count +=1

print("Count",count)
print("Sum", s)



#sample : http:// py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#실제 데이터: http://py4e-data.dr-chuck.net/comments_1512230.html (합계는 57로 끝남)