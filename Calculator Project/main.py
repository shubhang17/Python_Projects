import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
}

def calculator():
    should_accumulate = True
    number1 = float(input("Please Enter  the First Number: "))
    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operator = input("Please choice a operator: ")
        number2 = float(input("Please Enter  the Second Number: "))
        answer = operations[operator](number1,number2)
        print(f"{number1} {operator} {number2} = {answer}")


        choice = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation. ").lower()

        if choice == "y":
            number1 = answer
        elif choice != "y" and choice != "n":
            should_accumulate = False
            print("Thank YOu!")
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()



