# JTMS-14
# problem 6.1.py
# Abel Mengistu
# abmengistu@jacobs-university.de

f = open("input.txt", 'r') # opens file names input
text = f.read(1)
text2 = f.read(2)
print(ord(text)*ord(text2)) # coverts the characters
w = open("output.txt", 'w')
w.write(str(ord(text)*ord(text2)))
w.close()
f.close()
