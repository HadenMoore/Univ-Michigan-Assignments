"""9.4 Write a program to read through the mbox-short.txt and figure out who has
sent the greatest number of mail messages. The program looks for 'From ' lines
and takes the second word of those lines as the person who sent the mail. The
program creates a Python dictionary that maps the sender's mail address to a
count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop to find
the most prolific committer. """

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

mail = dict() 

for line in handle: 
    line = line.rstrip()
    #print(line)
    wds = line.split()
    #print(wds)
    for w in wds:
        mail[w] = mail.get(w, 0) +1 
        #print(w, 'new', mail[w])

#print(mail)

# Now to Find the Most Common Word
largest = -1
theword = None
for k, v in mail.items():
    # print(k,v)
    if v > largest:
        largest = v
        theword = k #Capture/Remember the KEY that was the Largest

print('Done', theword, largest)
