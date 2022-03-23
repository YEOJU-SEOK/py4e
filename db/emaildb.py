import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
# cursor 핸들같은것
cur = conn.cursor()

# 기존에 테이블 존재시 모두 삭제함
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('enter file name :')

if len(fname) < 1:
    fname = 'mbox-short.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    # '?' 사용자가 직접 입력한 문자열을 삽입함(자리를 표시해줌) -> sql injection 막아줌
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))

    # 추출한 레코드중 하나를 가져옴
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))

    conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# 종료
cur.close()
