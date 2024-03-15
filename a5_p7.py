# JTMS-14
# problem 5.7.py
# Abel Mengistu
# abmengistu@jacobs-university.de

s = input("Enter a string: ")
a = int(input("Enter an integer: "))
b = int(input("Enter an integer: "))
while not (a >= 0and b >= 0 and a < len(s)and b < len(s)):
    a = int(input("Enter an integer: "))
    b = int(input("Enter an integer: "))
print(s[a:b+1])
