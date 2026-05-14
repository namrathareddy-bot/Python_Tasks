"""Write a program to check whether a given number is Strong number"""

from math import factorial
def strong_number(num):
    s = 0
    total = 0
    original = num
    while num > 0:
        temp = num % 10
        num //= 10 
        s += factorial(temp)
    print(s)
    if original == s:
        print("It is a strong number")
    else:
        print("It is not a strong number")
strong_number(145)
