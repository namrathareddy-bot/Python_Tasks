"""5. Write a program to assign grades based on marks (for example:
A,B,C,Fail)"""
marks = int(input("enter marks: "))
if marks >= 80:
    print("A Grade")
elif marks >= 70:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
else:
    print("Fail")
