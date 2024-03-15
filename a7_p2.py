# JTMS-14
# problem 7.2.py
# Abel Mengistu
# abmengistu@jacobs-university.de

def main():
    translate("Merry Christmas and Happy New Year!")

def translate(list_en):
    inputs = {"Merry":"god", "Christmas":"jul", "and":"och", "Happy":"gott", "New":"nytt", "Year!":"\u00E5r!"}
    print(list_en, "in Swedish is: " )
    words = list_en.split()
    for word in words:
        ret = inputs.get(word,None)
        print(ret, end = " ")
    print()

main()
