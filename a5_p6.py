# JTMS-14
# problem 5.6.py
# Abel Mengistu
# abmengistu@jacobs-university.de

def count_vowels (s):
    num_vowels = 0
    for i in range (0, len(s)):
        if (s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u"):
            num_vowels = num_vowels+1
    return num_vowels

x = True
while x:
    s = input("Enter a string: ")
    if ( s== ""):
        x = False
    else:
        print("The number of vowels is: ",count_vowels(s))
print("Bye!")