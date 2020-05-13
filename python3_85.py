''' 
Collects email adrresses that start with "From ", 
prints it out, and then tells how many emails it found.
'''
# asks for a file name to open
fname = input("Enter file name: ")
fh = open(fname)
count = 0
# looks at each line and asks if it 
# starts with 'From '
for line in fh:
    if line.startswith('From '):
        l = line.split()
        print(l[1])
        count = count + 1
# returning the results of the programs search.
print("There were", count, "lines in the file with From as the first word")
