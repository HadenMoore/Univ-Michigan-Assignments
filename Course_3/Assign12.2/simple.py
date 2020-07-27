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
from bs4 import BeautifulSoup
import ssl

# Ignore SSL Certificate Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# To Retrieve all of the Anchor Tags: 
tags = soup('a')
for tag in tags:
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)





# # To Retrieve all <span> Tags: 
# tags = soup('')