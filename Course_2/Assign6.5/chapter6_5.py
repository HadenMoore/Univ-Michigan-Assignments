"""6.5 Write code using find() and string slicing (see section 6.10) to extract the
number at the end of the line below.
Convert the extracted value to a floating point number and print it out."""


str = "X-DSPAM-Confidence: 0.8475"

ipos = str.find(':')
# print(ipos)
piece = str[ipos+2:]
# print(piece)
# print(piece+42.0) # Will Fail.
value = float(piece)
print(value)
# print(value+42.0)

# Desired Output = 0.8475