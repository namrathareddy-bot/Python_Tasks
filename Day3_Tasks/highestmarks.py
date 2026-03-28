"""8. Write a program to find the student with the highest marks from a
dictionary."""
student_marks = {"abhimanyu":487,"krishna":560,"karna":600,"arjuna":512}
print("The student marks: ",student_marks)
topper = max(student_marks, key=student_marks.get)
print("The maximum marks is scored by: ",topper)
