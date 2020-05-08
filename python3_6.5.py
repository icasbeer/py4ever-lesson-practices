text = "X-DSPAM-Confidence:    0.8475"

numbers1 = text.find("0")
numbers2 = text.find("5")
print(numbers2)
ftnumbers = float(text[numbers1:numbers2+1])
print(ftnumbers)