#Calculator

from art import logo



#Add
def add(n1, n2):
    return n1 + n2

#Subtrac
def subtrac(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

#Guardar en diccionario
operations = {
    "+": add,
    "-": subtrac,
    "*": multiply,
    "/": divide
}

def calculator():

    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operations_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1, num2)

        print(f'{num1} {operations_symbol} {num2} = {answer}')

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()