# Running BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)

# <h1>An Interesting Title</h1>
# Note that this prints the first instance of an h1 tag found on the page.