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
def mult(a, b):
    return a * b

# Divide function
# a -- dividend
# b -- divisor
def div(a, b):
    return a / b


# -------------------------------------------------------- #


# -------------------------------------------------------- #
# -- MAIN FUNCTIONAILTY -- DO NOT EDIT ------------------- #
# -------------------------------------------------------- #

a = None
b = None
op = None
total = 0 # initialize total t ocontinue adding

#mode selection start
while True:
    mode = input("Enter '2' for continuous adding or '1' for basic operations: ").lower()  

    if mode == '2':  # continuous addition mode
        while True:
            a = input("Enter a number to add (or 'reset' to reset total, 'exit' to quit): ")  # start input
            if a.lower() == 'exit':  # exit option
                break
            elif a.lower() == 'reset':  # reset total option
                total = 0
                print("Total reset to 0.")
                continue
            try:
                a = float(a)  # make sure it's float
                total = add(total, a)  # add to running total
                print(f"Current Total: {total}")  # show current total
            except ValueError:
                print("Invalid number, please enter a valid number.")  # when invalid input

    elif mode == '1':  # basic  mode
        a = input("Enter the first argument: ")
        op = input("Enter the operation: ")
        b = input("Enter the second argument: ")
        try:
            a = float(a)  # make sure it's float
            b = float(b)  # make sure it's float
        except ValueError:
            print("Invalid number argument...")  # when invalid input
            continue

        # decide function
        if op != None:
            if op == "+":
                print("Sum: ", add(a, b))
            elif op == "-":
                print("Difference: ", sub(a, b))
            elif op == "*":
                print("Product: ", mult(a, b))
            elif op == "/":
                print("Quotient: ", div(a, b))
            else:
                print("Invalid operation...")

    else:
        print("Invalid mode. Please select '2' for continuous or '1' for single.")  # error handling


    q = input("Quit? [y/n] ")
    if (q == "y" or q == "Y"):
        break

# -------------------------------------------------------- #
