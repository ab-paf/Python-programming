# JTMS-14
# problem 3.7.py
# Abel Mengistu
# abmengistu@jacobs-university.de
x = 1
m= int(input("Enter minute: "))
while x <= m:
    if m==1:        # if-else is used to differentiate plural values from singular
        print(x,"minute = ",x*60, "seconds")
    else:
        print(x,"minutes = ",x*60, "seconds")
    x += 1
