def add(a, b):
    return a + b
def subtract(a, b):    
    return a - b
def multiply(a, b):   
    return a * b      
def divide(a, b):    
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b    
def power(a, b):     
     return a ** b
def modulus(a, b):   
     if b == 0:
        raise ValueError("Cannot modulus by zero")   
     return a % b
def floor_division(a, b):
    if b == 0:
        raise ValueError("Cannot floor divide by zero")
    return a // b
def main():
    print("Welcome to the calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Select an operator (+, -, *, /, **, %, //): ")
    try:
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        elif operator == '**':
            result = power(num1, num2)
        elif operator == '%':
            result = modulus(num1, num2)
        elif operator == '//':
            result = floor_division(num1, num2)
        else:
            print("Invalid operator. Please try again.")
            return
        print(f"The result is: {result}")
    except ValueError as e:
        print(f"Error: {e}. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")
       