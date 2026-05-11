"""2. Write a recursive function to find the nth Fibonacci number"""
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a,end = " ")
        a,b = b,a+b
fibonacci(10)
