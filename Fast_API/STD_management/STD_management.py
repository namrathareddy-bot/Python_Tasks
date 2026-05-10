from fastapi import FastAPI, HTTPException  # FastAPI framework + error handling
from pydantic import BaseModel  # For request body validation

app = FastAPI()  # Create FastAPI app instance

# -----------------------------
# Student Model (structure of data)
# -----------------------------
class Student(BaseModel):
    id: int | None = None   # ID will be auto-generated
    name: str               # Student name
    age: int               # Student age
    course: str            # Course name
    marks: int             # Marks obtained

# -----------------------------
# Temporary database (Python list)
# -----------------------------
students = []  # Stores all student records in memory
student_id_counter = 1  # Auto-increment ID generator

# -----------------------------
# 1. Add Student
# POST /students
# -----------------------------
@app.post("/students")
def add_student(student: Student):
    global student_id_counter  # Use global counter

    student.id = student_id_counter  # Assign unique ID
    student_id_counter += 1  # Increase ID for next student

    students.append(student)  # Save student in list

    return {"message": "Student added successfully"}  # Response

# -----------------------------
# 2. Get All Students
# GET /students
# -----------------------------
@app.get("/students")
def get_students():
    return students  # Return full list

# -----------------------------
# 3. Get Student by ID
# GET /students/{id}
# -----------------------------
@app.get("/students/{id}")
def get_student(id: int):
    for student in students:  # Loop through list
        if student.id == id:  # Match ID
            return student  # Return student data

    # If not found, show error
    raise HTTPException(status_code=404, detail="Student not found")

# -----------------------------
# 4. Update Student
# PUT /students/{id}
# -----------------------------
@app.put("/students/{id}")
def update_student(id: int, updated_student: Student):
    for index, student in enumerate(students):  # Get index + student
        if student.id == id:  # Find matching student

            updated_student.id = id  # Keep same ID
            students[index] = updated_student  # Replace old data

            return {"message": "Student updated successfully"}

    # If student not found
    raise HTTPException(status_code=404, detail="Student not found")

# -----------------------------
# 5. Delete Student
# DELETE /students/{id}
# -----------------------------
@app.delete("/students/{id}")
def delete_student(id: int):
    for index, student in enumerate(students):  # Loop list
        if student.id == id:  # Find student

            students.pop(index)  # Remove from list
            return {"message": "Student deleted successfully"}

    # If not found
    raise HTTPException(status_code=404, detail="Student not found")