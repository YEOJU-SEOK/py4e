import urllib.request, urllib.parse, urllib.error


fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    #decode과정 꼭 해줘야함
    print(line.decode().strip())


"""결과
But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
"""