# JTMS-14
# problem 8.3.py
# Abel Mengistu
# abmengistu@jacobs-university.de
def enqueue(x):
    inp = input("Please enter input: ")
    x.append(inp)
    print(inp, "enters")

def dequeue(x):
    x.pop(0)
    print(x.pop(0),"leaves")

def printq(x):
    print(x)