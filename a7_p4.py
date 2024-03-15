# JTMS-14
# problem 7.4.py
# Abel Mengistu
# abmengistu@jacobs-university.de

d = 7

tuple_lst = []
count = 0
while count < d:
    count +=1
    tuple_input = input("Please enter input: ")
    tuple_input = tuple_input.split()
    tuple_lst.append(tuple(tuple_input))

print(tuple_lst)

for i in range(d-1, -1, -1):
    if tuple_lst[i] == ():
        tuple_lst.pop(i)

print(tuple_lst)