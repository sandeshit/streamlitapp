import sqlite3
import json
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

# Function to insert data into the INTERNALDB table

class dbupdate:


    def __init__(self, db_name = 'new.db'):
        self.db_name = db_name


    def _connect(self):
        return sqlite3.connect(self.db_name)
    
    def jsodump(self, js):
        to_list = js.tolist()
        return json.dumps(to_list)

    def insertdata(self,hash, url, title, body, embedding):
        # Convert the embedding to a JSON string

        json_str = self.jsodump(embedding)

        # Connecting to sqlite
        conn = self._connect()


        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # Inserting data into the table
        cursor.execute('''INSERT INTO INTERNALDB (HASH, URL, TITLE, BODY, EMBEDDING) 
                        VALUES (?, ?, ?, ?, ?)''', (hash, url, title, body, json_str))

        # Commit your changes in the database
        conn.commit()

        # Closing the connection
        conn.close()

    def checkdata(self,hash):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('''SELECT TITLE, BODY FROM INTERNALDB WHERE HASH= ?''',(hash,))
        result = cursor.fetchone()
        conn.close()

        if result:
            return result
        else:
            return None, None

    def embdcompare(self,hash):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('''SELECT TITLE, EMBEDDING, URL FROM INTERNALDB''')
        results = cursor.fetchall()
        conn.close()
        hash = np.array(hash).reshape(1, -1)

        titles_and_embeddings = [(result[0], np.array(json.loads(result[1])), result[2]) for result in results]

        max_similarity = 0.0
        most_similar_title = None
        threshold = 0.4

        for title, stored_embedding, link in titles_and_embeddings:
            stored_embedding = stored_embedding.reshape(1, -1)
            similarity = cosine_similarity(hash, stored_embedding)[0][0]
            print(similarity)

            if similarity > threshold and similarity > max_similarity:
                max_similarity = similarity
                most_similar_title = title
                return_link = link

        # Print the most similar title if one was found above the threshold
        if most_similar_title:
            print(f"The most similar title is: {most_similar_title} with a similarity of {max_similarity}")
            return most_similar_title, return_link

        else:
            print("No similar title found above the threshold.")
            return None,None
        
        






