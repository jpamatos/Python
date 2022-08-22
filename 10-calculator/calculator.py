from art import logo
import os


def calculator():
    """Start Calculator"""
    print(logo)
    a = float(input("What is the first number? "))
    continuation(a)


def continuation(a):
    """Perform a calculation and show the result"""
    op = input("Pick an operation (+, -, *, /): ")
    b = float(input("Whats the second number? "))
    if op == "/" and b == 0:
        print("Error! You can't divide by zero! Try another number.")
        while b == 0:
            b = int(input("Whats the second number? "))
    function = operations[op]
    result = function(a, b)
    print(f"{a} {op} {b} = {result}")
    decision = input(f"Type 'y' to continue calcultating with {result}, or "
                     "type 'n' to start a new calculation, or 'x' "
                     "to exit: ").lower()
    if decision == "y":
        continuation(result)
    elif decision == "n":
        os.system("cls")
        calculator()
    elif decision == "x":
        return


def add(a, b):
    """a + b"""
    return a + b


def subtract(a, b):
    """a - b"""
    return a - b


def multiply(a, b):
    """a * b"""
    return a * b


def divide(a, b):
    """a / b"""
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

result = 0
calculator()
