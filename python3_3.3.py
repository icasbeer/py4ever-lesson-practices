s = input("Enter score:")
score = float(s)
if score <= 1.0 and score >= 0.0:
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    elif score < 0.6:
        print('F')
else:
    print('Score entered is not valid.')
    quit()
