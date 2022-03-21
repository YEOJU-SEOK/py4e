import urllib.request, urllib.parse

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#해당 파일에서 나온 단어의 갯수 체크를 위해 dict사용
counts = dict()

for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)