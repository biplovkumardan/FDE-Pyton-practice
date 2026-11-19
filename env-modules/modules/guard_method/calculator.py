def addition(a, b):
    return a + b

print("Calculator module is loaded.")

if __name__ == "__main__":
    print("This is a calculator module. Executing the addition function as a test:")
    print("Addition of 5 and 3 is:", addition(5, 3))


# when this condition is wrong, the code inside the if block will not be executed when the module is imported into another script. 
# This is a common practice to include test code or example usage in a module, while ensuring that it doesn't run when the module is imported 
# elsewhere.