'''
A program will prompt for a URL,
read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data,
compute the sum of the numbers in the file

Files below:
    Sample data: 'http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
    Actual data: 'http://py4e-data.dr-chuck.net/comments_1650656.json' (Sum ends with 70)
'''

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE






# info = json.loads(data)
# print('User count:', len(info))

# for item in info:
#     print('Name:', item['name'])
#     print('Id:', item['id'])
#     print('Attribute:', item['x'])