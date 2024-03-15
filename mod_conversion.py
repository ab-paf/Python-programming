# JTMS-14
# problem 8.3.py
# Abel Mengistu
# abmengistu@jacobs-university.de

def in2cm_table(startlength, stepsize, endlength):
    def convert(inch):
        conversion = inch*2.54
        return conversion
    print("{:>6} {:>10}".format('inch', 'cm'))

    counter = startlength
    while counter <= endlength:
        print("{:>6.1f} {:>10.1f}".format(counter, convert(counter)))
        counter += stepsize

