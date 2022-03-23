import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()
#테이블 생성
cur.executescript('''DROP TABLE IF EXISTS Artist;
                  DROP TABLE IF EXISTS Album;
                  DROP TABLE IF EXISTS Track;
                  
                  CREATE TABLE Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
                  
                  CREATE TABLE Album (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, artist_id INTEGER,
                  title TEXT UNIQUE);
                  
                  CREATE TABLE Track (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE, 
                  album_id INTEGER, len INTEGER, rating INTEGER, count INTEGER);''')


fname = input('enter file name: ')

if len(fname) < 1:
    fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')

for entry in all:
    if lookup(entry, 'Track ID') is None:
        continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Length')

    if name is None or artist is None or album is None:
        continue

    print(name, artist, album, count, rating, length)

    # ignore : 테이블에 동일한 값이 존재할 경우 해당 쿼리는 무시
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?,?)', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]

    # replace : 쿼리값이 존재할 경우 updatd 실행
    cur.execute('INSERT OR REPLACE INTO Track (title, album_id, len, rating, count) VALUES (?,?,?,?,?)',
                (album, album_id, length, rating, count))

    conn.commit()