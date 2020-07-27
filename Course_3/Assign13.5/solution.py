""" Extrracting Data from JSON
 In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py
 The program will prompt for a URL, read the JSON data from that URL
 using urllib and then parse and extract the comment counts from the JSON data, 
 compute the sum of the numbers in the file and enter the sum below:
 We provide two files for this assignment. One is a sample file where we give you the sum for your testing 
 and the other is the actual data you need to process for the assignment.
 Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
 Actual data: http://py4e-data.dr-chuck.net/comments_555677.json (Sum ends with 10)
 You do not need to save these files to your folder since your program will read the data directly from the URL
 Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
 """

import urllib, json
import urllib.request

while True: 
    url = input('Enter Location: ')
    if len(url) < 1: break

    print('Retrieving Data ', url)
    url_handle = urllib.request.urlopen(url)
    data = url_handle.read()

    print('Data Retrieved', len(data), "Characters")
    json_data = json.loads(data)
    
    com_count = len(json_data['comments'])
    print('Count: ', com_count)

    com_sum = 0 
    for comment in json_data['comments']:
        com_sum = com_sum + int(comment['count'])
    print('Sum: ', com_sum)