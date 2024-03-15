# JTMS-14
# problem 4.2.py
# Abel Mengistu
# abmengistu@jacobs-university.de

ch = input("Enter a character...")
n = int(input ("an integer"))

a = ord(ch) #number of initial ascii
for i in range(0 , n + 1):
    ch = chr(a)
    a = a+1
    print(ch)


