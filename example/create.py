import sqlite3
from example import bdata

dbase = sqlite3.connect('bdata.sqlite3') # Open a database File
print('Database opened')

dbase.execute(''' CREATE TABLE IF NOT EXISTS student(
    username VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    name TEXT NOT NULL,
    phone INT NOT NULL) ''')

print('Table created')
#dbase.execute('''INSERT INTO Student(username,password,name,phone)
 #      VALUES('21241A6737','21241A6737','Navya',7893267846)
#''')
cursor = dbase.cursor()

# Execute the SELECT query
#cursor.execute('DELETE from Student ')
#cursor.execute('Update Student set name="Nagula Navya Sri" where username="21241A6737"')
dbase.commit()
# Fetch all the rows and print them
cursor.execute('SELECT * from Student')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and the database connection
cursor.close()
dbase.close()
print('Database Closed')
