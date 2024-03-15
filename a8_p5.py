# JTMS-14
# problem 8.5.py
# Abel Mengistu
# abmengistu@jacobs-university.de

queue = ["Eric", "John", "Michael"]
queue.append("Terry")
queue.append("Graham")

#define the functions
def enqueue(x):
    inp = input("Please enter input: ")
    queue.append(inp)    # append adds element to the end of the list
    print(inp, "enters")

def dequeue(x):
    queue.pop(0)
    print(x.pop(0),"leaves")
''' pop removes element from list, in this case 
it will remove the element with index 0'''

def printq(x):
    print(x)

# call in functions
enqueue(queue)
dequeue(queue)
printq(queue)