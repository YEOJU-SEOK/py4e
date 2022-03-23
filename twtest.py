# 트위터 에서 친구 리스트 가져와 저장하는 로직(twurl이외의 파일 가져오지 않아서 실행은 안됨)
import json
from urllib.request import urlopen
import urllib.error
import twurl
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXIST Twitter (name TEXT, retrieved INTEGER, friends INTEGER)')

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('enter a twitter account, or quit : ')
    if acct == 'quit':
        break
    # 그냥 엔터 입력시
    if len(acct) < 1:
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            # 이름을 얻을 수 있음
            acct = cur.fetchone()[0]
        except:
            print('no unretrieved Twitter accounts found')
            continue

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
    print('retrieving', url)

    connection = urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('remaining', headers['x-rate-limit-remaining'])

    js = json.loads(data)

    cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct,))

    countnew = 0
    countold = 0

    for u in js['users']:
        friend = u['screen_name']
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend,))
        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',(count+1, friend))
            countold += 1
        # 친구에 대한 기록이 없다면 새로 추가해줌
        except:
            cur.execute('INSERT INTO Twitter (name, retrieved, friends)'
                        'VALUES (?, 0, 1)', (friend,))
            countnew += 1

    print('new accounts=', countnew, 'revisited=', countold)
    conn.commit()

cur.close()
