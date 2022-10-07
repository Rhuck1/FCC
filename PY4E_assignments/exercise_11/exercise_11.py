'''
A program to read through and parse a file with text and numbers. 
To extract all the numbers in the file and compute the sum of the numbers. 
'''
import re

file_name = input("Enter file name: ")

if len(file_name) < 1:
    file_name = 'test.txt'

try:
    file_handle = open(file_name)

except:
    print("File cannot be opened:", file_name)
    quit()

count = 0

for line in file_handle:

    line = line.rstrip()
    
    if re.search('[0-9]+', line):
        
        line_nums = re.findall('[0-9]+', line)

        sum = 0

        for str_num in line_nums:
          
            sum += int(str_num)

        count += sum

print(count)



    