'''
A program that will prompt for a URL,
read the XML data from that URL using urllib 
and then parse and extract the comment counts from the XML data,
compute the sum of the numbers in the file.

Files below:
    Sample data: 'http://py4e-data.dr-chuck.net/comments_42.xml' (Sum=2553)
    Actual data: 'http://py4e-data.dr-chuck.net/comments_1650655.xml' (Sum ends with 14)
'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(html)

print('Retrieving', url)

counts_list = tree.findall('.//count')

num_char_count = 0
sum = 0

for count in counts_list:

    sum += int(count.text)
    num_char_count += len(count.text)


print('Retrieved ' + str(num_char_count) + ' numerical characters')
print('Count:', len(counts_list))
print('Sum:', sum)