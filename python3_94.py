'''
finds the most recurring email in a peice of text.
'''
# Asks for the file and opens it.
fname = input("Enter file name: ")
fh = open(fname)
count = dict()

# Counts emails and throws them in a dictionary
for line in fh:
    if line.startswith('From '):
        L = line.split()
        l = L[1]
        if l in count:
            count[l] = count[l] + 1
        if l not in count:
            count[l] = 1

# finds the most recurring email address
max_val = 0
max_key = ''
for item in count.items():
    if item[1] > max_val:
        max_val = item[1]
        max_key = item[0]
print(max_key, max_val)