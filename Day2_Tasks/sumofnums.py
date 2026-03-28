"""3. Write a program to print the sum of numbers from 1 to N using loop."""
n = int(input("enter limit: "))
total = 0
for i in range(1,n+1):
    total += i
print(f"The sum of numbers from 1 to {n} is: {total}")
