# JTMS-14
# problem 10.2.py
# Abel Mengistu
# abmengistu@jacobs-university.de

from rational import Rational

s = Rational(1, 2)
d = Rational(1, 8)

print(s.__sub__(d))
print(s.__mul__(d))
print(s.__truediv__(d))


print("s==d: ", s==d)
print("s!=d: ", s!=d)
print("s<=d: ", s<=d)
print("s> d: ",  s>d)
print("s>=d: ", s>=d)