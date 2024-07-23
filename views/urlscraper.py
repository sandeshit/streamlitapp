import streamlit as st
from beautiful import scrape_page
from embeddings import sentencembd

st.title("WELCOME TO MLAPP")

# Input field for the URL
val = st.text_input("Enter the URL")

title = ""
body = ""
embd = []

# Button to trigger the scraping
if st.button("Enter"):
    if val:
        # Call the scrape_page function with the URL value
        title, body = scrape_page(val)
        embd = sentencembd(title)
    else:
        st.error('Please enter a URL.')

# Optionally, you can print the URL in the Streamlit app instead of using print()
st.write(f"URL passed to scrape_page: {val}")
st.write(title)
st.write(body)

print(embd)
