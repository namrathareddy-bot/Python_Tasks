"""4. Write a program to perform left shift and right shift operations on a
number."""
num1 = int(input("enter number: "))
num2 = int(input("enter number: "))
left_shift = num1<<num2
right_shift = num1>>num2
print(f"The left shift for {num1} and {num2} is: ",left_shift)
print(f"The right shift for {num1} and {num2} is: ",right_shift)
