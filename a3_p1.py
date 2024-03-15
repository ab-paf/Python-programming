# JTMS-14
# problem 3.1.py
# Abel Mengistu
# abmengistu@jacobs-university.de

min = int(input("Please enter a number: "))
if min >= 0:                #checks if the input is valid
    hours = min//60
    min= min%60             #calculates the remiander to be minutes
    print("it's ",hours," hours and",min,"minutes.")
else:
    print("You have entered an invalid input")