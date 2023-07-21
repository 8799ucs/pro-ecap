import sqlite3

abase = sqlite3.connect('tdata.sqlite3') # Open a database File
print('Database opened')

abase.execute(''' CREATE TABLE IF NOT EXISTS teacher(
    username VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    name TEXT NOT NULL,
    phone INT NOT NULL) ''')

print('Table created')

cursor=abase.cursor()

# Execute the SELECT query
#cursor.execute('SELECT * from Teacher where username="1675"')
cursor.execute('DELETE from Teacher ')
cursor.execute('SELECT * from Teacher')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and the database connection
cursor.close()
abase.close()
print('Database Closed')