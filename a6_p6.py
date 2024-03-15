# JTMS-14
# problem 6.6.py
# Abel Mengistu
# abmengistu@jacobs-university.de

def histogram(lst):
    for i in lst:
        print('*'*i)
lst = []
n = int(input('Enter number of elements:'))

for i in range(0,n):
    ele = int(input('Enter element:'))
    lst.append(ele)
histogram(lst)