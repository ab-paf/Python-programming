# JTMS-14
# problem 8.1.py
# Abel Mengistu
# abmengistu@jacobs-university.de

startlength = float(input("Enter a start length here: "))
stepsize = float(input("Enter a step size here: "))
endlength = float(input("Enter an end length here: "))

def convert(inch):
    conversion = inch*2.54
    return conversion
print("{:>6} {:>10}".format('inch', 'cm'))

counter = startlength
while counter <= endlength:
    print("{:>6.1f} {:>10.1f}".format(counter, convert(counter)))
    counter += stepsize