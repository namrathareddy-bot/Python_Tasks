# 3. Write a program to check whether a number is a Palindrome.

num=input("Enter a number: ")

if num==num[::-1]:
    print("It is a Palindrome")
else:
    print("Not a Palindrome")
