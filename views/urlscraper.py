import streamlit as st
from beautiful import scrape_page
from embeddings import sentencembd
import hashlib
from dbupdate import dbupdate

ab= dbupdate()

st.title("WELCOME TO MLAPP")

# Input field for the URL
val = st.text_input("Enter the URL")

title = ""
body = ""
embd = []

# Button to trigger the scraping
if st.button("Enter"):
    if val:
        result1 = hashlib.md5(val.encode('utf-8'))
        hash = result1.hexdigest()
        title,body = ab.checkdata(hash)
        if not title:
            title, body = scrape_page(val)
            embd = sentencembd(title)
            ab.insertdata(hash,val,title,body,embd)

        st.write(f"URL passed to scrape_page: {val}")
        st.write(title)
        st.write(body)


    else:
        st.error('Please enter a URL.')

# Optionally, you can print the URL in the Streamlit app instead of using print()

#print(embd)
