# 1. Write a program to check whether a given number is an Armstrong number or not.

num=int(input("Enter a number: "))

num_str= str(num)
n=len(num_str)

total = sum(int(digit) ** n for digit in num_str)

if num == total:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
t
