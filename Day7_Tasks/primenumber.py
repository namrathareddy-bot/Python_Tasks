"""Write a program to check whether a number is prime or not"""

def prime_num(num):
    if num <= 1:
        print("Its not prime number")
    else:
        for i in range(2,num):
            if num % i == 0:
                print("Its not prime number")
                return
        print("Its prime number")
prime_num(5)
