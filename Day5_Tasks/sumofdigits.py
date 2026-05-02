"""3. Write a recursive function to calculate the sum of digits of
a number.
Example: Input = 123 ---> Output = 6"""
def sum_of_digits(n):
    temp = 0
    while n>0:
        temp += n%10
        n = n//10
    print("The sum of digits is: ",temp)
sum_of_digits(123)
        
    
