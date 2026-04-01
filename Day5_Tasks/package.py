"""A company wants to organize its Python code using packages.
Create a package named utilities that contains two modules:
● math_operations.py (functions for addition and multiplication)
● string_operations.py (functions to convert string to uppercase and count characters)
Write a Python program that imports the package and uses functions from both modules."""

from utilities import math_operations
print("For Default values")
print("Sum is ",math_operations.add(2,4))
print("Multiplication is ",math_operations.mul(2,4))

from utilities import string_operations

print("Uppercase is ",string_operations.upper('abcd'))
print("Character count is ",string_operations.counting("xyz"),'\n')

x=int(input("Enter a number "))
y=int(input("Enter another number "))
print("Sum is ",math_operations.add(x,y))
print("Multiplication is ",math_operations.mul(x,y),'\n')

s=str(input("Enter only characters "))
print("Uppercase is ",string_operations.upper(s))
print("Character count is ",string_operations.counting(s),'\n')
