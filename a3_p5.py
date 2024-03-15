# JTMS-14
# problem 3.5.py
# Abel Mengistu
# abmengistu@jacobs-university.de
v = input("Enter a lower case:")
asc = ord(v)
if 97 <= asc <= 122:    # defines the range for block letters in the ASCII table
    print("It's a lower case!")     # print out if input is correct
else:
    print("Not a lower case!")      # print out if input is incorrect