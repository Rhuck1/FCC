'''
A program will use urllib to read the HTML from the data files below, 
extract the href= vaues from the anchor tags, 
scan for a tag that is in a particular position relative to the first name in the list,
follow that link and repeat the process a number of times and report the last name you find.

Files below:
    Sample data: http://py4e-data.dr-chuck.net/known_by_Fikret.html (Last name in sequence: Anayah)
    Actual data: http://py4e-data.dr-chuck.net/known_by_Ashleigh.html (The first character of the name of the last page that you will load is: O)
    
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
for tag in tags:

    # Loops through tag and prints desired tag aspect
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)