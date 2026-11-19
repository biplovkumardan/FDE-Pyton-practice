from addition import addition # importing the addition function from the addition module (addition.py file)
from subtraction import subtraction # importing the subtraction function from the subtraction module (subtraction.py file)
from multiplication import multiplication # importing the multiplication function from the multiplication module (multiplication.py file)   
from division import division # importing the division function from the division module (division.py file)



def main():
    print("Addition:", addition(10, 5))
    print("Subtraction:", subtraction(10, 5))
    print("Multiplication:", multiplication(10, 5))
    print("Division:", division(10, 5))

if __name__ == "__main__": # guard to ensure the main function is called only when the script is run directly
    main()