● Addition
● Subtraction
● Multiplication
● Division
Then write another Python program that imports this module
and performs calculations based on user input."""
import calculator
print("Note: Only two numbers are used for this program")
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print("The addition of two numbers is: ",calculator.add(a,b))
print("The subtraction of two numbers is: ",calculator.subtract(a,b))
print("The multiplication of two numbers is: ",calculator.multiply(a,b))
print("The division of two numbers is: ",calculator.divide(a,b))
