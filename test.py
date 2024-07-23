import sqlite3

conn = sqlite3.connect('new.db')

cursor = conn.cursor()

cursor.execute('''SELECT TITLE FROM INTERNALDB''')

result = cursor.fetchall()
print(result)