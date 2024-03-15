# JTMS-14
# problem 8.2.py
# Abel Mengistu
# abmengistu@jacobs-university.de

startlength = float(input("Enter a start length here: "))
stepsize = float(input("Enter a step size here: "))
endlength = float(input("Enter an end length here: "))

def cmconvert(inch):
    cmconversion = inch*2.54
    return cmconversion
print("{:<6} {:>8} {:>8} {:>8}".format('inch', 'cm', 'm', 'km'))

def mconvert(inch):
    mconversion = inch*0.0254
    return mconversion

def kmconvert(inch):
    kmconversion = inch*0.000254
    return kmconversion

nf = open('table.txt', 'w')
nf.write("{:<5} {:>5} {:>10} {:>10},\n".format('inch','cm','m','km'))

counter = startlength
while counter <= endlength:
    nf.write("{:<5} {:>5} {:>10.4f} {:>10.7f},\n".format(counter, cmconvert(counter),mconvert(counter),kmconvert(counter)))
    counter += stepsize