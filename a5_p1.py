# JTMS-14
# problem 5.1.py
# Abel Mengistu
# abmengistu@jacobs-university.de
def to_liter(gallon, cup):
    convert = gallon*3.7854 + cup*0.2366 # does the actual conversion
    return convert
cup = float(input("Enter value in cups: "))
gallon = float(input("Enter value in gallons: "))

result = to_liter(gallon,cup) #prints outside the function
print("The conversion of ", cup, " cups and ", gallon, "gallons is ", result, "liters.")
