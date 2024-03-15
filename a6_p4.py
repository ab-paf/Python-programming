# JTMS-14
# problem 6.4.py
# Abel Mengistu
# abmengistu@jacobs-university.de
x = input('Enter file name:')
f = open(x+'.txt', 'r')
text = f.read()
w = open('copy.txt', 'w')
w.write(text)
f.close()
w.close()