# JTMS-14
# problem 8.4.py
# Abel Mengistu
# abmengistu@jacobs-university.de

from mod_conversion import in2cm_table
from mod_conversion4 import in2cm_html

startlength = float(input("Enter a start length here: "))
stepsize = float(input("Enter a step size here: "))
endlength = float(input("Enter an end length here: "))

check_s = input('Please enter a character: ')

if check_s == 's':
    print(in2cm_table(startlength,stepsize,endlength))
else:
    print(in2cm_html(startlength,stepsize, endlength))

