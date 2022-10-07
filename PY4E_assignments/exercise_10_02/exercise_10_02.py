'''
A program to read through the mbox-short.txt and figure out the
 distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time 
and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

file_name = input("Enter file name: ")

try:
    file_handle = open(file_name)

except:
    print("File cannot be opened:", file_name)
    quit()

d = {}

for line in file_handle:

    line = line.rstrip()

    if not line.startswith("From "):
        continue

    split_line = line.split()

    for word in split_line:

        if ':' not in word:
            continue

        time = word.split(':')
        hour = time[0]

        if hour in d:

            d[hour] += 1

        else:

            d[hour] = 1

sorted_d = sorted(d.items())

for key, val in sorted_d:
    print(key, val)



