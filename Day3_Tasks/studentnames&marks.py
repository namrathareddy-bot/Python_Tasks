"""1. Create a dictionary with 3 student names and their marks."""
n = 3
d = {}
for i in range(1,n+1):
    names = input(f"enter student name {i}: ")
    marks = int(input("enter marks of student: "))
    d[names] = marks
print(d)
