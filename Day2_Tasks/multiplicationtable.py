"""2. Write a program to print the multiplication table of a number
using a loop"""
num = int(input("enter number to print multiplication table: "))
j = 1
for j in range(1,11):
    print(f"{num}*{j}= {num*j}")
