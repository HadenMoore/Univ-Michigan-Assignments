# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

""" The program will use urllib to read the HTML 
from the data files below, and parse the data, extracting numbers and 
compute the sum of the numbers in the file.
Files: 
Sample Data: http://py4e-data.dr-chuck.net/comments_42.html (Sum = 2553)
Actual Data:  http://py4e-data.dr-chuck.net/comments_555454.html (Sum Ends with 95) """

import urllib.request, urllib.parse, urllib.error
from bs4 import *
import ssl

# Ignore SSL Certificate Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

"""Acutal Data link for Coursera AutoGrader: http://py4e-data.dr-chuck.net/comments_555674.html (Sum Ends with 35)
url = 'http://py4e-data.dr-chuck.net/comments_555674.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")"""

#Acutal Data link for PY4E AutoGrader: http://py4e-data.dr-chuck.net/comments_555454.html (Sum Ends with 95)
url = 'http://py4e-data.dr-chuck.net/comments_555674.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve All <span> Tags: 
spans = soup('span')

# Calculate a Sum of All Numbers in Span Tags: 
sum = 0
for span in spans: 
    sum = sum + int(span.contents[0])
print(sum)




"""
# To Retrieve all of the Anchor Tags: 
tags = soup('a')
for tag in tags:
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
"""