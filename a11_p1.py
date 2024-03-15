# JTMS-14
# problem 11.1.py
# Abel Mengistu
# abmengistu@jacobs-university.de

while True: #
    name = input("Enter file name: ")

    try:
        file = open(name, "r")
        for a in file:
            print(a, end="")
        file.close()
        break # ends the loop if the input is valid

    except FileExistsError as nothing:
        print(nothing) # prints error message if the file does not exist
    except FileNotFoundError as kaput:
        print(kaput) # prints error message if the file cannot be found
    except OSError as err:
        print(err)
    else:
        file.close()