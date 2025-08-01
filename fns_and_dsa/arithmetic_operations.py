
def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform an arithmetic operation between two numbers.

    Parameters:
        num1 (float): First operand.
        num2 (float): Second operand.
        operation (str): The operation to perform - 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float or str: The result of the operation, or an error message if division by zero or invalid operation.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
