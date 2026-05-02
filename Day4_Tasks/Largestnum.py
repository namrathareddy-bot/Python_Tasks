"""10. Write a python program with a function that returns the largest of
three numbers."""
def largest_number():
    num1 = int(input("enter number 1: "))
    num2 = int(input("enter number 2: "))
    num3 = int(input("enter number 3: "))
    if num1==num2 and num2==num3 and num3==num1:
        print("All numbers are same.")
    elif num1 > num2 and num1 > num3:
        print(f"The number {num1} is greater.")
    elif num2 > num1 and num2 > num3:
        print(f"The number {num2} is greater.")
    else:
        print(f"The number {num3} is greater.")
largest_number()
