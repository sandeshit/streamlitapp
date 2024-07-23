import requests
from bs4 import BeautifulSoup
root = 'https://reliefweb.int'
#val = 'https://reliefweb.int/report/occupied-palestinian-territory/child-casualties-west-bank-skyrocket-past-nine-months-enar'




import newspaper
# Define the website URL




def scrape_page(url):
    print("URL:", url)
    r = newspaper.Article(url="%s" % (url))
    r.download()
    r.parse()

    body = r.text
    print('------------')
    title = r.title

    return title,body


       





