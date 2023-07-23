import sqlite3
from example import tdata

abase = sqlite3.connect('tdata.db') # Open a database File
print('Database opened')

abase.execute(''' CREATE TABLE IF NOT EXISTS Teacher(
    username VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    name TEXT NOT NULL,
    phone INT NOT NULL) ''')

print('Table created')
abase.execute('''INSERT INTO Teacher(username,password,name,phone)
       VALUES('1675','1675','Annapoorna','6304643005')
''')
abase.execute('''INSERT INTO Teacher(username,password,name,phone)
       VALUES('1741','1741','Dr.Mv.Ramasundari','9441518001')
''')
abase.execute('''INSERT INTO Teacher(username,password,name,phone)
       VALUES('1747','1747','Mr.N.Devendhar','9704741266')
''')
abase.execute('''INSERT INTO Teacher(username,password,name,phone)
       VALUES('1700','1700','Mr.K.Arun','9908024556')
''')
abase.execute('''INSERT INTO Teacher(username,password,name,phone)
       VALUES('1704','1704','Dr.E.Poornima','9391695656')
''')
abase.execute('''INSERT INTO Teacher(username,password,name,phone)
       VALUES('1621','1621','Ms.M.Shamila','9533065054')
''')
abase.commit()
cursor=abase.cursor()
cursor.execute('SELECT * from Teacher')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and the database connection
cursor.close()
abase.close()
print('Database Closed')
