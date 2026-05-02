"""2. Write a program to check if one number is greater than another. """
num1 = int(input("enter number: "))
num2 = int(input("enter number: "))
if num1 == num2:
    print("Both numbers are same.")
elif num1 > num2:
    print(f"{num1} is greater than {num2}.")
else:
    print(f"{num2} is greater than {num1}.")
