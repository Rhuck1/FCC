'''
A code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.
'''

text = "X-DSPAM-Confidence:    0.8475"

col_pos = text.find(':')

iso_text = text[col_pos + 1:]

flt_val = float(iso_text)

print(flt_val)