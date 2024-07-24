import streamlit as st
import hashlib
from embeddings import sentencembd
from dbupdate import embdcompare

st.title("This is the search page")

titl= st.text_input("Enter the title you want to search")


title = ""
body = ""
embd = []

# Button to trigger the scraping
if st.button("Enter"):
    if titl:
        embd = sentencembd(titl)
        ret = embdcompare(embd)
        
        st.write(f"Query passed to the search: {titl}")
        st.write(ret)


    else:
        st.error('Please enter a URL.')
