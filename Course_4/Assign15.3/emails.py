import sqlite3
import urllib
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

#Indicating the file (URL)
fname = "http://www.pythonlearn.com/code3/mbox.txt"
fh = urllib.request.urlopen(fname)

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Getting the top 10 results and showing them
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print("Counts:")
for row in cur.execute(sqlstr) :
    print(str(row[0]), row[1])
    
cur.close()