"""9. Write a program that checks if two numbers are equal.   
10. Combine arithmetic and comparison operators in one expression. """

#9. Write a program that checks if two numbers are equal.
num1 = 10
num2 = 10
if num1 == num2:
    print(f"Numbers are equal. That is {num1}")
else:
    print(f"Numbers are not equal. That is {num1} and {num2}")
print("-------------------------------------------------------------\n")

#10. Combine arithmetic and comparison operators in one expression.

a = 10
b = 5
# Combining arithmetic (+) and comparison (>)
result = (a + b) > 12

print("Result:", result)
