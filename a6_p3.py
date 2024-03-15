# JTMS-14
# problem 6.3.py
# Abel Mengistu
# abmengistu@jacobs-university.de

g = input("File name: ")
x = open(g+".txt", 'r')
count = 0
for i in x:
    count +=1
    word = i.split()
    wordcount = len(word)
    print("In line ", count, "there are", wordcount, "words")