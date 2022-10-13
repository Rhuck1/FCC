'''
A program that will use urllib to read HTML from data files, 
parse the data, extracting the numbers and computing their sum

Files below:
    Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
    Actual data: http://py4e-data.dr-chuck.net/comments_1650653.html (Sum ends with 86)

'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

samp_url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url = 'http://py4e-data.dr-chuck.net/comments_1650653.html'

file_handle = urllib.request.urlopen(samp_url)

for line in file_handle: print(line.decode().strip())