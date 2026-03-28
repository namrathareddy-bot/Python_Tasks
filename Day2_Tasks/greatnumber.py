"""3. Write a program to find the largest of three numbers using if-elif-else"""
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
num3 = int(input("enter number 3: "))
if num1 == num2 and num2 == num3 and num3 == num1:
    print(f"{num1},{num2} and {num3} are equal")
elif num1 > num2 and num1 > num3:
    print(f"{num1} is greater than the other.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is greater than the other. ")
else:
    print(f"{num3} is greater than the other. ")
    
