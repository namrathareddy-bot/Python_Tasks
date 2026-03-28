"""1. Write a program to check whether a number is
positive,negative or zero"""
number = int(input("enter number: "))
if number == 0:
    print("The number entered is zero.")
elif number > 0:
    print("The number is a positive number.")
else:
    print("The number is a negative number.")
