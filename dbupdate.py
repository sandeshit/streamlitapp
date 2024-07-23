import sqlite3
import json

# Function to insert data into the INTERNALDB table
def insertdata(hash, url, title, body, embedding):
    # Convert the embedding to a JSON string

    embed_tolist = embedding.tolist()
    json_str = json.dumps(embed_tolist)

    # Connecting to sqlite
    conn = sqlite3.connect('new.db')

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Inserting data into the table
    cursor.execute('''INSERT INTO INTERNALDB (HASH, URL, TITLE, BODY, EMBEDDING) 
                      VALUES (?, ?, ?, ?, ?)''', (hash, url, title, body, json_str))

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()

def checkdata(hash):
    conn = sqlite3.connect('new.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT TITLE, BODY FROM INTERNALDB WHERE HASH= ?''',(hash,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return result
    else:
        return None, None





