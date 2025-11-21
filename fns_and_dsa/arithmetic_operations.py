def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs one of the four basic arithmetic operations ('add', 'subtract', 
    'multiply', or 'divide') on two numbers.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform. Must be one of the four 
                         specified strings.

    Returns:
        float or str: The result of the operation as a float, or the 
                      string "Error: Cannot divide by zero" if division 
                      by zero is attempted.
    """
    
    # Standardize the operation input to handle case-insensitivity (e.g., 'ADD' or 'Add')
    op = operation.lower() 

    if op == 'add':
        # Addition
        return num1 + num2
    
    elif op == 'subtract':
        # Subtraction
        return num1 - num2
    
    elif op == 'multiply':
        # Multiplication
        return num1 * num2
    
    elif op == 'divide':
        # --- Critical Requirement: Division by Zero Handling ---
        if num2 == 0:
            # Return a specific string that main.py can check for
            return "Error: Cannot divide by zero"
        else:
            return num1 / num2
            
    else:
        # Handle cases where the operation string is not recognized
        return f"Error: Invalid operation '{operation}'. Use 'add', 'subtract', 'multiply', or 'divide'."