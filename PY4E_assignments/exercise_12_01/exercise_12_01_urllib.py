'''
A program using urllib to retrieve the following document
using the HTTP protocol in a way that the HTTP Response 
headers can be examined:

    http://data.pr4e.org/intro-short.txt
'''

import urllib.request

url = 'http://data.pr4e.org/intro-short.txt'

file_handle = urllib.request.urlopen(url)