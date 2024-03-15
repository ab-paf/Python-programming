# JTMS-14
# problem 10.4.py
# Abel Mengistu
# abmengistu@jacobs-university.de


from students import Student
import random

s1 = Student("Sam",1)
s2 = Student("keke",2)
s3 = Student("jim",4)
s4 = Student("Pam",2)
s5 = Student("Mike",1)
s6 = Student("Nikita",2)
s7 = Student("Issa",3)
s8 = Student("Jeff",3)
s9 = Student("Jon",5)
s10 = Student("Max",2)

s_lst = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
print(random.shuffle(s_lst))

print("\nThe Unsorted list is:")
i = 0
for s in s_lst:
    i += 1
    print(i, ',', s.getName())

s_lst = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
s_lst.sort(reverse=True)

print("\nThe sorted list is:")
j = 0
for s in s_lst:
    j += 1
    print(j,",", s.getName())

