def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a/b

def main():
    print("Addition:", addition(10, 5))
    print("Subtraction:", subtraction(10, 5))
    print("Multiplication:", multiplication(10, 5))
    print("Division:", division(10, 5))

if __name__ == "__main__": # guard to ensure the main function is called only when the script is run directly
    main()