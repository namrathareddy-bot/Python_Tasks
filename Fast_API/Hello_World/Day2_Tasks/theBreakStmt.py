"""1. Write a program using break to stop printing numbers when the number
reaches 5."""
num = int(input("enter limit: "))
for i in range(1,num+1):
    if i == 5:
        break
    print(i)
