# JTMS-14
# problem 7.3.py
# Abel Mengistu
# abmengistu@jacobs-university.de

n = int(input("Enter a number here: "))


v = []
w = []

countv = 0
while  countv < n:
    tupinpv = float(input("Enter a number for tuple v: "))
    countv += 1
    v.append(tupinpv)

countw = 0
while countw < n:
    tupinpw = float(input("Enter a number for tuple w: "))
    countw += 1
    w.append(tupinpw)

v = tuple(v)
w = tuple(w)


print (v)
print (w)

def scalar(tup1,tup2):
    scalar = 0
    for i in range (n):
       scalar += tup1[i] * tup2[i]
    return scalar

print(scalar(v,w))