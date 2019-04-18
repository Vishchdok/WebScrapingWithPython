# Connecting Reliably and Handling Exceptions
# Handling HTTP Errors
# HTTP Errors such as 404 Page Not Found or 500 Internal Server Error

from urllib.request import urlopen
from urllib.error import HTTPError

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    # return null, break, or do some other "Plan B"
else:
    # program continues. Note: If you return or break in the
    # exception catch, you do not need to use the "else" statement
    print("Success!")