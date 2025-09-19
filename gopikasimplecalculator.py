

def calculator():
    print("Simple Calculator - Let's Do Some Math! 😄\n")

    print("Options: +  -  *  /")

    try:
        a = float(input("Enter first number (a): "))

        b = float(input("Enter second number (b): "))

        op = input("Choose operation (+, -, *, /): ")

        match op:

            case '+':
                print(f"Result: {a} + {b} = {a + b}")

            case '-':
                print(f"Result: {a} - {b} = {a - b}")

            case '*':
                print(f"Result: {a} * {b} = {a * b}")

            case '/':
                if b != 0:
                    print(f"Result: {a} / {b} = {a / b}")
                else:
                    print("Error: Can't divide by zero 😅")

            case _:
                print("Invalid choice. Please use +, -, *, or /.")

    except ValueError:
        print("Numbers only! Letters won't work here. 🤓")


calculator()
