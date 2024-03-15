# JTMS-14
# problem 6.1.py
# Abel Mengistu
# abmengistu@jacobs-university.de

f = open("numbers.txt", 'r')
sum = 0
for line in f:
    line = line.strip()
    number = int(line)
    sum += number
print("The sum is", sum)
f.close()