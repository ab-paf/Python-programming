# JTMS-14
# problem 7.7.py
# Abel Mengistu
# abmengistu@jacobs-university.de

def main():
    sampleDict = {'Python': 82, 'OR': 85, 'PMS': 75, 'Management': 70, 'Chemistry': 72}

    key = input("Enter a key: ")
    x = sampleDict.get(key,None)

    if x == None:
        print("Doesn't exist: ")
    else:
        print("Value of key is:", x)

main()