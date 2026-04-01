# 1. Student Attendance Record A teacher wants to store student attendance in a file named attendance.txt. Write a Python program that takes a student name as input and appends it to the file. Then display the contents of the file.

std_name=input("Enter student name: ")

f=open("Attendance.txt","a")

f.write(std_name+"\n")
f.close()

f1=open("Attendance.txt","r")
print(f1.read())

f.close()
