import streamlit as st
from embeddings import sentencembd
from dbupdate import dbupdate

db = dbupdate()

st.title("This is the search page")

titl= st.text_input("Enter the title you want to search")


title = ""
body = ""
embd = []

# Button to trigger the scraping
if st.button("Enter"):
    if titl:
        embd = sentencembd(titl)

        ret, link = db.embdcompare(embd)
        if ret:
            st.markdown(f"[{ret}]({link})")

        st.write(f"Query passed to the search: {titl}")


    else:
        st.error('Please enter a URL.')
