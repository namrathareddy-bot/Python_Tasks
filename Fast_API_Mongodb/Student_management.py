# ============================================================
# 📝 FastAPI Student Management App
# MongoDB Atlas + MongoEngine
# pip install fastapi uvicorn mongoengine pymongo
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import (
    connect,
    Document,
    IntField,
    StringField,
    FloatField
)

# ------------------------------------------------------------
# 🚀 FastAPI App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🌐 MongoDB Atlas Connection
# ------------------------------------------------------------
MONGO_URL = "mongodb+srv://johnnyysg05_db_user:swetha1234@test.wmpbutc.mongodb.net/student_db?retryWrites=true&w=majority"

connect(host="mongodb+srv://johnnyysg05_db_user:swetha1234@test.wmpbutc.mongodb.net/student_db?retryWrites=true&w=majority")

# ------------------------------------------------------------
# 🧱 MongoDB Model
# ------------------------------------------------------------
class StudentDB(Document):
    student_id = IntField(primary_key=True)
    name = StringField(required=True)
    age = IntField(required=True)
    course = StringField(required=True)
    marks = FloatField(required=True)

    meta = {
        "collection": "students"
    }

# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------
class Student(BaseModel):
    student_id: int
    name: str
    age: int
    course: str
    marks: float

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------
@app.get("/")
def home():
    return {"message": "FastAPI Student Management System 🚀"}

# ------------------------------------------------------------
# ✅ 1. CREATE STUDENT
# ------------------------------------------------------------
@app.post("/students")
def create_student(student: Student):

    # Check duplicate student ID
    existing = StudentDB.objects(
        student_id=student.student_id
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )

    new_student = StudentDB(
        student_id=student.student_id,
        name=student.name,
        age=student.age,
        course=student.course,
        marks=student.marks
    )

    new_student.save()

    return {
        "message": "Student created successfully",
        "data": student
    }

# ------------------------------------------------------------
# ✅ 2. READ ALL STUDENTS
# ------------------------------------------------------------
@app.get("/students")
def get_all_students():

    students = StudentDB.objects()

    data = []

    for student in students:
        data.append({
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age,
            "course": student.course,
            "marks": student.marks
        })

    return {
        "count": len(data),
        "data": data
    }

# ------------------------------------------------------------
# ✅ 3. READ SINGLE STUDENT
# ------------------------------------------------------------
@app.get("/students/{student_id}")
def get_student(student_id: int):

    student = StudentDB.objects(
        student_id=student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "student_id": student.student_id,
        "name": student.name,
        "age": student.age,
        "course": student.course,
        "marks": student.marks
    }

# ------------------------------------------------------------
# ✅ 4. UPDATE STUDENT
# ------------------------------------------------------------
@app.put("/students/{student_id}")
def update_student(student_id: int, updated: Student):

    student = StudentDB.objects(
        student_id=student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = updated.name
    student.age = updated.age
    student.course = updated.course
    student.marks = updated.marks

    student.save()

    return {
        "message": "Student updated successfully"
    }

# ------------------------------------------------------------
# ✅ 5. DELETE STUDENT
# ------------------------------------------------------------
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    student = StudentDB.objects(
        student_id=student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.delete()

    return {
        "message": "Student deleted successfully"
    }

# ============================================================
# ▶️ Run Command
# ============================================================
# uvicorn filename:app --reload
#
# Example:
# uvicorn main:app --reload
# ============================================================