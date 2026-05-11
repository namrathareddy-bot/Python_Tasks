"""5. Write a program that prints numbers from 1 to 10 but skips
even numbers using continue."""
n = 10
for i in range(1,n+1):
    if i%2 == 0:
        continue
    print(i,end = " ")
    
