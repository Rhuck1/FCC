'''
A program to open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split() method.
The program should build a list of words.
For each word on each line check to see if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.

You can download the sample data at http://www.py4e.com/code3/romeo.txt
'''

file_name = input("Enter file name: ")

try:
    file_handle = open(file_name)

except:
    print("File cannot be opened:", file_name)
    quit()

lst = []

for line in file_handle:

    line = line.rstrip()

    split_line = line.split()

    for word in split_line:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)