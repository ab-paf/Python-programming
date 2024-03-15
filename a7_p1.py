# JTMS-14
# problem 7.1.py
# Abel Mengistu
# abmengistu@jacobs-university.de

def longest_word(lst):
    longest__word = ''
    for word in lst:
        if len(word) > len(longest__word):
            longest__word = word
    return longest__word

words = input("Enter random words: ")
lst = words.split()
word = longest_word(lst)
word_length = len(word)
print(word, word_length)