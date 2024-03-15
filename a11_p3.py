# JTMS-14
# problem 11.3.py
# Abel Mengistu
# abmengistu@jacobs-university.de

class FormulaError(Exception): pass

def maths(ab):
    sign = ["+", "-"]
    if len(ab) != 3: # sets rule for at least 3 elements to be input
        raise FormulaError("Formula Error: Input doesn't consist of 3 element")
    elif ab[1] not in sign:
        raise FormulaError("Formula Error: Only + or - is allowed")
    else:
        try:
            num1 = float(ab[0])
            num2 = float(ab[2])
            if ab[1] == "+":
                return num1 + num2
            else:
                return num1 - num2
        except ValueError as ess: # exception for value error created
            raise FormulaError(ess)


i = 1

while i:
    # asking for the input
    formula = input("Enter num '+'/'-' num: ")
    b = formula.split()
    # try and exception to carry out the operation
    try:
        print(formula, "=", maths(b))
    except FormulaError as err:
        print(err)

    prompt = input("Type 'quit' if you want to exit: ")
    if prompt.lower() == "quit":
        i = 0
        print("Thank you")