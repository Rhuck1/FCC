'''
A program will use urllib to read the HTML from the data files below, 
extract the href= vaues from the anchor tags, 
scan for a tag that is in a particular position relative to the first name in the list,
follow that link and repeat the process a number of times and report the last name you find.

Files below:
    Sample data: http://py4e-data.dr-chuck.net/known_by_Fikret.html (Last name in sequence: Anayah)
    Actual data: http://py4e-data.dr-chuck.net/known_by_Ashleigh.html (The first character of the name of the last page that you will load is: O)

'''

from socketserver import BaseRequestHandler
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

'''
The program below uses a range loop to accomplish the task
'''

url = input('Enter URL: ')
process = int(input('Enter process loops: '))
position = int(input('Enter position: '))

# print(f'Retrieving: {url}')

# url_list = []
# tag_list = []
# content_list = []

# for index in range(process):

#     html = urllib.request.urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')
    
#     tags = soup('a')

#     process_counter = 0
#     position_counter = 0

#     for tag in tags:

#         position_counter += 1
#         if position_counter == position:
#             url = str(tag.get('href', None))
#             print(f'Retrieving: {url}')
#             url_list.append(url)
#             tag_list.append(tag)
#             content_list.append(tag.contents[0])
#             position_counter = 0
#             break

# print("-----------------------------")
# print('URL List:', url_list)
# print("-----------------------------")
# print('Tag List:', tag_list)
# print("-----------------------------")
# print('Content List:', content_list)
# print("-----------------------------")
# print('Final Name:', content_list[-1])

'''
The program below uses a while loop to accomplish the task
'''

url_list = []
tag_list = []
content_list = []

process_count = 0

while process_count < process:

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    position_counter = 0

    for tag in tags:
        
        position_counter += 1
        if position_counter == position:

            print('Retrieving: ', url)
            url = str(tag.get('href', None))
            url_list.append(url)
            tag_list.append(tag)
            content_list.append(tag.contents[0])
            position_counter = 0
            process_count += 1
            break

print("-----------------------------")
print('URL List:', url_list)
print("-----------------------------")
print('Tag List:', tag_list)
print("-----------------------------")
print('Content List:', content_list)
print("-----------------------------")
print('Final Name:', content_list[-1])