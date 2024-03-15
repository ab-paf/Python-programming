# JTMS-14
# problem 4.3.py
# Abel Mengistu
# abmengistu@jacobs-university.de

#while True:
   # ch = input("Enter a char: ")
 #   asc = ord(ch)
   # if 65 <= asc <= 90:    # defines the range for block letters in the ASCII table
   #     break    # print out if input is correct
         # print out if input is incorrect

ch = input("Enter char:")
asc = ord(ch)
while asc < 65 or asc > 90:
    ch = input("Enter char:")
    asc = ord(ch)
n = 33
while n < 0 or n > 32:
    n = int(input("Enter int: "))

a = ord(ch) #number of initial ascii
for i in range(0, n + 1):
    ch = chr(a)
    a = a+1
    print(ch)