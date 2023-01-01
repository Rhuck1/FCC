'''
This application will read the mailbox data (mbox.txt) 
and count the number of email messages per organization 
(i.e. domain name of the email address) 
using a database with the following schema to maintain the counts:

            CREATE TABLE Counts (org TEXT, count INTEGER)

The data file for this application is: http://www.py4e.com/code3/mbox.txt
'''


import sqlite3

conn = sqlite3.connect('mboxdb')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

for line in fh:

    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]

    cur.execute('SELECT count from FROM Counts WHERE email = ?', (email, ))
    row = cur.fetchone()

    if row is None:
        cur.execute('''INSERT INTO Coutns (email, count)
            VALUES (?, 1)''', (email, ))

    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email, ))

    conn.commit()

sqlstr = 'SELECT email, count from Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()