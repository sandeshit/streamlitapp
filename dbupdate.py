import sqlite3
import json
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

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

def embdcompare(hash):
    conn = sqlite3.connect('new.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT TITLE, EMBEDDING FROM INTERNALDB''')
    results = cursor.fetchall()
    conn.close()
    hash = np.array(hash).reshape(1, -1)

    titles_and_embeddings = [(result[0], np.array(json.loads(result[1]))) for result in results]

    max_similarity = 0.0
    most_similar_title = None
    threshold = 0.4

    for title, stored_embedding in titles_and_embeddings:
        stored_embedding = stored_embedding.reshape(1, -1)
        similarity = cosine_similarity(hash, stored_embedding)[0][0]
        print(similarity)

        if similarity > threshold and similarity > max_similarity:
            max_similarity = similarity
            most_similar_title = title

    # Print the most similar title if one was found above the threshold
    if most_similar_title:
        print(f"The most similar title is: {most_similar_title} with a similarity of {max_similarity}")
    else:
        print("No similar title found above the threshold.")
    
    return most_similar_title






