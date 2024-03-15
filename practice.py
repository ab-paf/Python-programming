size = int(input("Enter a number: "))
for i in range (size):
    for j in range (i + 1):
        print(chr(j + 65), end= '')
    print()


w= "this is sentence"

def substitute_vowels(x, ch):
    newstr = ""
    for i in x:
        if i in "aeiouAEIOU":
            newstr += ch
        else:
            newstr += i
    return newstr
n = substitute_vowels(w, "o")
print(n)

def substitute_vowels(str, ch):
    vowels = "aeiou"
    new_str = ""
    for i in str:
        if i in vowels:
            new_str += ch
        else:
            new_str += i
    return new_str

s = "This is a sentence"
print(s)
n = substitute_vowels(s, 'o')
print(n)