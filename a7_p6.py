# JTMS-14
# problem 7.2.py
# Abel Mengistu
# abmengistu@jacobs-university.de

def main():
    sampleDict = {'Physics': 82, 'Math': 85, 'History':75, 'Management':70, 'Chemistry':72}
    print("Min value =", min_value(sampleDict))

def min_value(dic):
    minimum = min(dic.values())
    for key in dic:
        if dic[key] == minimum:
            return key
main()