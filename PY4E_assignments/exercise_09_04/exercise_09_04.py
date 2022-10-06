'''
A program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

file_name = input("Enter file name: ")

try:
    file_handle = open(file_name)

except:
    print("File cannot be opened:", file_name)

d = {}

for line in file_handle:

    line = line.rstrip()

    if not line.startswith("From "):
        continue

    split_line = line.split()

    email_address = split_line[1]

    if email_address in d:

        d[email_address] += 1
    
    else:
        d[email_address] = 1

greatest = 0
author = None

for key, val in d.items():
    if val < greatest:
        continue
    else:
        greatest = val
        author = key

print()

print(d)
print("The most prolific author is", author, "with", d[author])