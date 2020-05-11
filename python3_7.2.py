# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
average = 0.0
N = 0 # Total number
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    stripped_line = float(line[20:27])
    average = average + stripped_line
    N += 1
average = average/N
print('Average spam confidence:', average)
