num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operation = input("Choose the operation(+,-,*,/): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            exit()
        else:
            result = num1 / num2

print(f"The result is {result}.")

