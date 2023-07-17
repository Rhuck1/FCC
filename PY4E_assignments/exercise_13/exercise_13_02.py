'''
A program will prompt for a URL,
read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data,
compute the sum of the numbers in the file

Files below:
    Sample data: 'http://py4e-data.dr-chuck.net/comments_42.json' (Sum=2553)
    Actual data: 'http://py4e-data.dr-chuck.net/comments_1650656.json' (Sum ends with 70)
'''

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
data = json.loads(html)

print('Retrieving', url)

num_char_count = 0
sum = 0

for item in data['comments']:

    sum += item['count']
    for char in str(item['count']):
        num_char_count += 1
    

print('Retrieved ' + str(num_char_count) + ' numerical characters')
print('Count:', len(data['comments']))
print('Sum:', sum)