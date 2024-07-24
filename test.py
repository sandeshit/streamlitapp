import sqlite3

conn = sqlite3.connect('new.db')

cursor = conn.cursor()

cursor.execute('''SELECT TITLE FROM INTERNALDB''')

j = 0

result = cursor.fetchall()
for i in result:
    
    print(f'{j}.{i}')
    print("-----")
    j+=1

