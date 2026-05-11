"""2. Write a program using continue to skip printing the number 3 in
a loop from 1 to 10."""
num = int(input("enter limit: "))
i = 0
for i in range(1,num+1):
    if i == 3:
        continue
    print(i,end = " ")
