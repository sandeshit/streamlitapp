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


       





