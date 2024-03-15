# JTMS-14
# problem 7.5.py
# Abel Mengistu
# abmengistu@jacobs-university.de

tuple_lst = []
n = int(input("Enter a number: "))
while n > 0:
    tuple_lst.append(n)
    n = int(input("Enter an integer: "))

print(tuple_lst)

tuple_lst.reverse()
reversetup = tuple(tuple_lst)
print(reversetup)