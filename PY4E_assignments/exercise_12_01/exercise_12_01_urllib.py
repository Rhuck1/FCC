'''
A program using urllib to retrieve the following document
using the HTTP protocol in a way that the HTTP Response 
headers can be examined:

    http://data.pr4e.org/intro-short.txt
'''

import urllib.request

url = 'http://data.pr4e.org/intro-short.txt'

file_handle = urllib.request.urlopen(url)

# This is the code to print the headers requested per the assignment
headers = file_handle.getheaders()

for head in headers:

    if head[0] == 'Last-Modified': 
        print('Last-Modified:', head[1])

    elif head[0] == 'ETag':
        print('ETag:', head[1])

    elif head[0] == 'Content-Length':
        print('Content-Length:', head[1])

    elif head[0] == 'Cache-Control':
        print('Cache-Control:', head[1])

    elif head[0] == 'Content-Type':
        print('Content-Type:', head[1])


# Below code will print out only txt from url    
# for line in file_handle:

#     print(line.decode().strip())