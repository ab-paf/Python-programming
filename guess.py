import random
random.seed()
minval =1
maxval = 100
r =random.randint(minval,maxval)
found =False
while not found:
    guess = int(input("ENTER YOUR GUESS: "))
    if r == guess:
        print("You got it!")
        found = True
    elif guess < r:
        print("Your guess is too small!")
    else :
        print("Your guess is too high!")
print("Bye!")