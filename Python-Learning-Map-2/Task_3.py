#Exercise 1

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    else:
        return result

print(safe_divide(100, 3))  
print(safe_divide(15, 0)) 


#Exercise 2

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")
            
        print(f"Result: {result}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the calculator
calculator()