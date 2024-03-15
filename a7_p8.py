# JTMS-14
# problem 7.8.py
# Abel Mengistu
# abmengistu@jacobs-university.de

def push (s,v):
    print('Pushing', v)
    s.append(v)
def pop (s):
    if (len(s) == 0):
        print('Slack Overflow')
        return
    else:
        print('Popping', s[-1])
        return s,pop()

def empty (s):
    print("Emptying stack")
    for i in range(len(s)):
        pop(s)

stack = []
sinput = input("Enter a character: ")
while sinput != 'q':
    if sinput == 's':
        num = int(input("Enter a number: "))
        push(stack, num)
    elif sinput == 'p':
        pop(stack)
    elif sinput == 'e':
        empty(stack)

sinput = input("Enter a character: ")
print("Good Bye!")