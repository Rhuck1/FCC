'''
A program that will use urllib to read HTML from data files, 
parse the data, extracting the numbers and computing their sum

Files below:
    Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
    Actual data: http://py4e-data.dr-chuck.net/comments_1650653.html (Sum ends with 86)

'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:

    # Loops through tag and prints desired tag aspect
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)

    count += int(tag.contents[0])

print(count)