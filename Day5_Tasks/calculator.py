"""calculator.py
1. Addition
2. Subtraction
3. Multiplication
4. Division
"""
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "Cannot divide number by zero"
    return a/b
