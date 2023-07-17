'''
A simple program that utilizes the json parser to 
demonstrate the parsing of simple a json string.
'''

import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print('Name:', info['name'])
print('Hide:', info['email']['hide'])