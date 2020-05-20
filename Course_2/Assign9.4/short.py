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

for lin in handle: 
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:
        # This prints the Word before
        print(w)
        if w in mail: 
            mail[w] = mail[w] + 1
            # Prints whether it is Existing
            print('**Existing**')
        else: 
            mail[w] = 1
            # Prints whether it is New
            print('**NEW**')
        print(mail[w])
        # This prints the Count After