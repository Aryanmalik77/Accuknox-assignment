from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(
    title="Student Test Scores API",
    description="REST API providing student test scores for Problem Statement 1 - Question 2"
)

class Student(BaseModel):
    student_name: str
    marks_obtained: int

students_db = [
    {"student_name": "Alice", "marks_obtained": 85},
    {"student_name": "Bob", "marks_obtained": 92},
    {"student_name": "Charlie", "marks_obtained": 78},
    {"student_name": "Diana", "marks_obtained": 88},
    {"student_name": "Evan", "marks_obtained": 95},
    {"student_name": "Fiona", "marks_obtained": 82},
    {"student_name": "George", "marks_obtained": 90}
]

@app.get("/api/students/", response_model=List[Student])
@app.get("/api/students", response_model=List[Student])
def get_students():
    """Returns the list of students and their marks."""
    return students_db

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
