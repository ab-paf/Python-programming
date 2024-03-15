min = int(input("Please enter a number: "))
if min >= 0:
    hours = min//60
    min= min%60
    print("it's ",hours,"and",min,"minutes.")
else:
    print("You have entered invalid input")