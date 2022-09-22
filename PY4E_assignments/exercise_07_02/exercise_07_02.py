'''
A program that prompts for a file name, then opens that file and reads through the file, 
looking for lines of the form:

< X-DSPAM-Confidence:    0.8475 >

Count these lines and extract the floating point values from each of the lines 
and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt,
 when you are testing below enter mbox-short.txt as the file name.
'''

file_name = input("Enter file name: ")

try:
    file_handle = open(file_name)

except:
    print('File cannot be opened:', file_name)
    quit()

count = 0
spam_count = 0

for line in file_handle:

    line = line.rstrip()

    if not line.startswith("X-DSPAM-Confidence"):
        continue

    count += 1    
    col_pos = line.find(':')

    iso_text = line[col_pos + 1:]

    flt_val = float(iso_text)

    spam_count += flt_val

print("Average spam confidence:", spam_count / count)

