# Take a number as input from the user. If the number is greater than 0, print 'Positive'. If it is less than 0, print 'Negative'. Otherwise print 'Zero'

num = int(input("Enter a number\n"))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")