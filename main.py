# DEFINE MATHEMATICAL FUNCTIONS
def add(n1, n2):
    """Returns the sum of two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Returns the difference of two numbers."""
    return n1 - n2

def multiply(n1, n2):
    """Returns the product of two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Returns the division of two numbers. Handles division by zero."""
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1 / n2

# Dictionary of operators
operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    """
    A simple command-line calculator that performs basic operations: 
    Addition (+), Subtraction (-), Multiplication (*), and Division (/).
    
    Users can input expressions like '2 + 3' instead of separate numbers.
    """
    print("Welcome to the Python Calculator!")
    print("Enter 'exit' to quit.")
    
    while True:
        try:
            user_input = input("\nEnter calculation (e.g., 5 + 3): ").strip().lower()
            if user_input == "exit":
                print("Goodbye!")
                break
            
            # Split user input into components
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid format. Use format: number operator number (e.g., 5 + 3)")
                continue

            num1, operation, num2 = parts
            num1, num2 = float(num1), float(num2)

            # Perform calculation
            if operation in operators:
                result = operators[operation](num1, num2)
                print(f"Result: {num1} {operation} {num2} = {result}")
            else:
                print("Invalid operator. Please use +, -, *, or /.")

        except ValueError:
            print("Invalid input. Please enter numbers and a valid operator.")

if __name__ == "__main__":
    calculator()
