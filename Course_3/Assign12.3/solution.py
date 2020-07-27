"""Following Links in Python

In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
scan for a tag that is in a particular position relative to the first name in the list, 
follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and 
the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. 
The answer is the last name that you retrieve.

Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah

Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Jiorrja.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.

Hint: The first character of the name of the last page that you will load is: I
"""

import urllib.request
import re
import sys
sys.path.append("/Users/haden/Documents/Michigan/Univ-Michigan-Assignments/Course_3/Assign12.3/bs4/")
from bs4 import *
import ssl

url = input('Enter URL: ')
count = int(input('Enter Count: '))
position = int(input('Enter Position: '))

while count >= 0: 
    name = re.findall('known_by_(.+).html', url)
    print('Retrieving Information: ' + url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieving 'a' Tags: 
    links = soup('a')
    url = links[position -1 ].get('href', None)
    count = count - 1

    print('Last Name Found: ' + name[0])
