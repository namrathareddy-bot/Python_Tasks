"""6. Write a function that returns the factorial of a number."""
def fact():
    num = int(input("enter number: "))
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    print("The factorial of a number is: ",fact)
fact()
