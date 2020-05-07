'''
This program is meant to take a set of numbers and compute
the minimum and maximum numbers after typing in "done".

Isaac Casbeer
5/7/2020
'''
#defines the largest and smallest values
largest = None
smallest = None
#starts a loop to take in values
while True:
    #asks for an input
    num = input("Enter a number: ")
    #runs a set of directions with a failsafe in case of an error
    try:
        #converts input to integer
        num = int(num)
        #compares input to the largest and smallest values
        if largest == None or smallest == None:
            largest = num
            smallest = num
        else: 
            if num > largest:
                largest = num
            if num < smallest:
                smallest = num
    #if an error occurs, it runs this code and goes to the start of the loop
    except:
        if num == 'done':
            break 
        else:
            print('Invalid input')
#returns the maximum and minimum
print("Maximum", largest)
print('Minimum', smallest)