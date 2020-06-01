import re
fh = open('test_data.txt')
total = 0
for line in fh:
    numlst = re.findall('[0-9]+', line) 
    for value in numlst:
        value = int(value)
        total = value + total

print(total)