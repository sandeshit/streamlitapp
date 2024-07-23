import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('new.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Creating table as per requirement
sql ='''CREATE TABLE INTERNALDB (
   Id INTEGER PRIMARY KEY AUTOINCREMENT,
   HASH VARCHAR(30) NOT NULL,
   URL VARCHAR,
   TITLE VARCHAR(50),
   BODY VARCHAR(5000),
   EMBEDDING VARCHAR(1000)
)'''
cursor.execute(sql)
print("Table created successfully........")

# Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()