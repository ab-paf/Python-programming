sentence = input ("Enter a sentence: ")
listofwords = sentence.split( '$')
listofwords = "12 444 666".split( ' ')
print("There are", len(listofwords), "words.")
print(listofwords)
sum = 0
for word in listofwords:
    print(word)
    sum += len(word)
print("The average word length is", sum / len(listofwords))