'''
Program finds file and organizes characters alphabetically.
'''
#finding file
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
#turning into list
for line in fh:
    a = line.split()
    #adding and filtering incoming strings
    for string in a:
        if string not in lst:
            lst.append(string)
# alphabetically sorts the list 
# and then prints it            
lst.sort()
print(lst)