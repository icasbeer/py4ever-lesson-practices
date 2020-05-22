'''
takes the hour the email was emailed and
 tells how many times it shows up
'''
fname = input("Enter file name: ")
fh = open(fname)
count = dict()
#     Goes through each line and splits it up
# and then takes the hour and increases the times 
# the computer has seen it by one
for line in fh:
    if line.startswith('From '):
        l = line.split(':')
        l0 = l[0].split()
        l5 = l0[5]
        if l5 in count:
            count[l5] = count[l5] + 1
        if l5 not in count:
            count[l5] = 1
lst = sorted(count)
for val in lst:
    print(val, count[val])
