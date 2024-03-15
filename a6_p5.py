# JTMS-14
# problem 6.5.py
# Abel Mengistu
# abmengistu@jacobs-university.de
def add(lst, val):
    x = [p + val for p in lst]
    return x

def multiply(lst, val):
    y = [p * val for p in lst]
    return y

n = int(input('Enter number of elements:'))

data = []
i = 1
while i <= n:
    ele = int(input('Enter element:'))
    data.append(ele)
    i+=1

print(data)
print(add(data, 1.5))
print(multiply(data, 5))
