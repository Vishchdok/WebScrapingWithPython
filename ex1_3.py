# Connecting Reliably and Handling Exceptions
# Handling URL Errors
# URL Errors such as server isn't found or URL is mistyped

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It worked!')