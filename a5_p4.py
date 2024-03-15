# JTMS-14
# problem 5.3.py
# Abel Mengistu
# abmengistu@jacobs-university.de
import random
random.seed()
minval = 1
maxval = 50
r = random.randint(minval,maxval)
found = False
while not found:
    guess = int(input("Enter  your  guess: "))
    if r == guess:
        break
        print("You got the number!")
        #found = True
    elif guess < r:
        print("Your guess is too small!")
    else:
        print("Your guess is too high!")
print("Bye!")