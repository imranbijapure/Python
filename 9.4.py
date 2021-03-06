##Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#  The program creates a Python dictionary that maps the sender's mail address to a count of
# the number of times they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.

# ENTER THE FILE
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
text = handle.read()
words = list()
#KEP ONLY THE EMAILS STARTING FROM;
#KEEPING ONLY EMAILS
for line in handle:

    if not line.startswith('From:'): continue
    line = line.split()
    words.append(line[1])
#USING THE DICTIONARY TO STORE THE EMAILS
counts = dict()

for word in words:
    counts[word] = counts.get(word, 0) + 1

#COUNT THE BIGGEST NUMBER USED

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword, bigcount

