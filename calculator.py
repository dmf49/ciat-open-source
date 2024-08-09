import sys

# -------------------------------------------------------- #
# -- CALCULATOR FUNCTIONS -------------------------------- #
# -------------------------------------------------------- #

# Add function
# a -- addend
# b -- augend
def add(a, b):
    return a + b

# Subtract function
# a -- minuend
# b -- subtrahend
def sub(a, b):
    return a - b

# Multiply function
# a -- multiplicand
# b -- multiplier
#def mult(a, b):
#    return a * b

# Divide function
# a -- dividend
# b -- divisor
#def div(a, b):
#    return a / b


# -------------------------------------------------------- #


# -------------------------------------------------------- #
# -- MAIN FUNCTIONAILTY -- DO NOT EDIT ------------------- #
# -------------------------------------------------------- #

a = None
b = None
op = None

while (True):
    # get input values
    a = input("Enter the first argument: ")
    op = input("Enter the operation: ")
    b = input("Enter the second argument: ")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print ("Invalid number argument...")
        op = None

    # decide function
    if (op != None):
        if (op == "+"):
            print (f"the sum of {a} and {b} is: {add(a, b)}") # added  f to format the string
        elif (op == "-"):
            print (f"the difference of {a} and {b} is: {sub(a, b)}") # added  f to format the string
        elif (op == "*"):
            print (f"the product of {a} and {b} is: {mult(a, b)}") # added  f to format the string
        elif (op == "/"):
            print (f"the quotient of {a} and {b} is: {div(a, b)}") # added  f to format the string
        else:
            print ("Invalid operation...")

    q = input("Quit? [y/n] ")
    if (q == "y" or q == "Y"):
        break

# -------------------------------------------------------- #