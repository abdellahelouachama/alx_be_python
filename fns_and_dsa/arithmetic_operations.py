def perform_operation(num1, num2, operation):
    if operation == 'add':
        return float(num1 + num2)
    elif operation == 'subtract':
        return float(num1 - num2)
    elif operation == 'multiply':
        return float(num1 * num2)
    else:
        
        return float(num1 / num2)
        # else:
        #     return f"Cannot divide by {float(num2)}."
                      